from typing import Dict, List, Optional, Any
import os, json, re
from dotenv import load_dotenv
from openai import OpenAI
from common.logger import get_logger

logger = get_logger("agent.resume.unresolved")

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


SECTIONS = [
    "identity",
    "profile",
    "education",
    "experience",
    "projects",
    "skills",
    "tools",
    "certifications",
    "languages",
    "awards",
    "publications",
    "volunteer",
    "other"
]

def build_unresolved_prompt(
    unresolved_text: str,
    sections: list[str],
) -> str:
    return f"""
You are helping to clean and organize a CV.

The text below could not be classified by rule-based code.
Your task is ONLY to assign it to the most appropriate existing section(s).

Existing CV sections:
{", ".join(sections)}

Section definitions:
- identity: name, title, role.
- profile: professional summary, career objective.
- education: degrees, universities, GPA.
- experience: work experience, internships.
- projects: personal or academic projects with descriptions.
- skills: abstract skills, methods, concepts, domains.
- tools: concrete software/tools only (e.g., Git, VS Code, Jupyter).
- certifications: certificates, exams.
- languages: spoken languages.
- awards: honors, awards.
- publications: papers, articles.
- volunteer: volunteer activities.
- other: anything else.

Rules:
- Preserve original wording exactly.
- Do NOT rewrite, summarize, or fix grammar.
- If multiple sections exist, split into multiple blocks.
- Each block MUST belong to exactly ONE section.
- Use ONLY section names listed.
- Do NOT invent new sections.
- ALL input text MUST be assigned.
- Do NOT add explanations.

Output format (plain text ONLY):

[section_name]
original text

[another_section_name]
original text

Text to classify:
----------------
{unresolved_text}
----------------
"""


def resolve_unresolved(
    structured: Dict[str, str],
    unresolved_text: str,
    model: str = "gpt-4o-mini",
) -> Dict[str, str]:
    """
    Use LLM to route unresolved CV text into existing sections (TEXT ONLY).
    LLM writes to delta only, then merged with structured (dedup + guard).
    """

    if not unresolved_text.strip():
        return structured

    # 1. LLM delta must cover ALL valid sections (not only existing structured keys)
    llm_delta: Dict[str, str] = {k: "" for k in SECTIONS}

    prompt = build_unresolved_prompt(
        unresolved_text=unresolved_text,
        sections=SECTIONS,
    )

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        output = resp.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"LLM unresolved routing failed: {e}")
        return structured

    # 2. Parse LLM output: [section] blocks
    pattern = re.compile(
        r"\[([a-zA-Z_]+)\]\s*(.*?)(?=\n\[[a-zA-Z_]+\]|\Z)",
        re.S,
    )
    matches = pattern.findall(output)

    if not matches:
        logger.error("LLM unresolved routing failed: no section blocks found")
        return structured

    for section, text in matches:
        section = section.strip().lower()
        if section not in llm_delta:
            section = "other"

        cleaned = text.strip()
        if not cleaned:
            continue

        llm_delta[section] += ("\n\n" + cleaned) if llm_delta[section] else cleaned

    # 3. Merge delta -> structured (dedup + semantic guard)
    for section, new_text in llm_delta.items():
        if not new_text.strip():
            continue

        if section not in structured:
            structured[section] = ""

        existing = structured[section].strip()

        # hard dedup
        if existing and new_text in existing:
            continue

        # semantic guard for tools
        if section == "tools":
            if any(x in new_text.lower() for x in [
                "pipeline", "workflow", "rag", "orchestration", "retrieval"
            ]):
                # redirect to skills
                target = "skills"
                if target not in structured:
                    structured[target] = ""
                if new_text not in structured[target]:
                    structured[target] += (
                        "\n\n" + new_text
                        if structured[target].strip()
                        else new_text
                    )
                continue

        structured[section] += (
            "\n\n" + new_text
            if structured[section].strip()
            else new_text
        )

    logger.info("Unresolved text successfully routed and merged by LLM")
    return structured

