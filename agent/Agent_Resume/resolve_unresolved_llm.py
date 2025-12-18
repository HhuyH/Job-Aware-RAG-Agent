# File này **dùng LLM để phân loại phần `unresolved` vào đúng section CV**, áp dụng khi rule-based không xử lý được, **giữ nguyên text gốc**, 
# parse output theo block `[section]`, rồi **merge có dedup (đặc biệt với projects)** vào cấu trúc CV hiện có.

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


def resolve_unresolved(structured: Dict[str, str], unresolved_text: str, model: str = "gpt-4o-mini") -> Dict[str, str]:
    """
    Use LLM to route unresolved CV text into existing sections (TEXT ONLY).
    Projects dedup based on project title keywords.
    """

    if not unresolved_text.strip():
        return structured

    llm_delta = {k: "" for k in SECTIONS}

    prompt = build_unresolved_prompt(unresolved_text, SECTIONS)

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

    # Parse output: [section] blocks
    pattern = re.compile(r"\[([a-zA-Z_]+)\]\s*(.*?)(?=\n\[[a-zA-Z_]+\]|\Z)", re.S)
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

    # Merge delta -> structured with dedup logic
    for section, new_text in llm_delta.items():
        if not new_text.strip():
            continue
        if section not in structured:
            structured[section] = ""

        existing = structured[section].strip()

        # Special dedup for projects: check title keywords
        if section == "projects":
            titles_existing = re.findall(r"Project\s+([^\n—–]+)", existing)
            titles_new = re.findall(r"Project\s+([^\n—–]+)", new_text)
            # Only append new_text if it contains at least one new title
            if all(title in titles_existing for title in titles_new):
                continue

        # Basic string dedup for other sections
        if existing and new_text in existing:
            continue

        structured[section] += ("\n\n" + new_text) if existing else new_text

    logger.info("Unresolved text successfully routed and merged by LLM")
    return structured
