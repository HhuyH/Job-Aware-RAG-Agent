from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import re
from common.logger import get_logger
from pathlib import Path
from common.json_logger import dump_json

logger = get_logger("agent.resume.extraction")

@dataclass
class Project:
    title: str
    role: Optional[str]
    description: str
    technologies: List[str]
    signals: Dict[str, bool]

@dataclass
class Certification:
    name: str
    score: Optional[str]

@dataclass
class SkillItem:
    name: str
    level: str  # core | exposure | familiar

@dataclass
class SkillSet:
    languages: List[SkillItem]
    frameworks: List[SkillItem]
    ml: List[SkillItem]
    databases: List[SkillItem]

@dataclass
class Tool:
    name: str

# Trích xuất kỹ năng từ text dựa trên tập từ khóa đã định nghĩa
def extract_skills(text: str) -> SkillSet:
    SECTION_MAP = {
        "programming languages": "languages",
        "frameworks": "frameworks",
        "frameworks & technologies": "frameworks",
        "ai / machine learning": "ml",
        "database": "databases",
    }
    
    LEVEL_HINTS = {
        "core": ["core", "strong", "primary"],
        "exposure": ["optional", "exposure", "familiar", "basic"]
    }

    skills = {
            "languages": [],
            "frameworks": [],
            "ml": [],
            "databases": [],
    }

    current_category = None
    current_level = "core"

    for line in text.splitlines():
        l = line.lower().strip()

        # detect section
        for header, cat in SECTION_MAP.items():
            if header in l:
                current_category = cat
                current_level = "core"
                break

        # detect level
        for level, hints in LEVEL_HINTS.items():
            if any(h in l for h in hints):
                current_level = level

        # extract bullet list
        if current_category and ("•" in line or "," in line):
            items = re.split(r"[•,]", line)
            for item in items:
                name = item.strip()
                if name and len(name) > 1:
                    skills[current_category].append(
                        SkillItem(name=name, level=current_level)
                    )

    return SkillSet(**skills)

def extract_tools(text: str) -> List[Dict[str, str]]:
    TOOLS = [
        "github",
        "jupyter notebook",
        "google colab",
        "vscode",
        "vs code",
        "android studio",
        "sql server management studio",
        "ssms",
    ]
    
    found = set()
    lower_text = text.lower()

    for tool in TOOLS:
        # match whole phrase, tránh dính chữ
        pattern = r"\b" + re.escape(tool) + r"\b"
        if re.search(pattern, lower_text):
            # normalize output name
            name = tool

            if tool in ("vscode", "vs code"):
                name = "VS Code"
            elif tool == "ssms":
                name = "SQL Server Management Studio"
            else:
                name = tool.title()

            found.add(name)

    return [{"name": t} for t in sorted(found)]

# Trích xuất chứng chỉ từ text
def extract_certifications(text: str) -> List[Certification]:
    CERT_PATTERN = re.compile(
        r"""
        (?P<name>TOEIC|IELTS|JLPT|HSK|CEFR)
        [^\d]{0,10}
        (?P<score>\d{2,4})?
        """,
        re.IGNORECASE | re.VERBOSE
    )

    certs = []

    for line in text.splitlines():
        m = CERT_PATTERN.search(line)
        if m:
            certs.append(
                Certification(
                    name=m.group("name").upper(),
                    score=m.group("score")
                )
            )
    return certs

# Dự đoán các tín hiệu kỹ thuật từ mô tả project
def infer_project_signals(text: str) -> Dict[str, bool]:
    lower = text.lower()

    return {
        "llm": any(k in lower for k in ["llm", "gpt", "rag", "langchain"]),
        "backend": any(k in lower for k in ["api", "fastapi", "flask", "backend"]),
        "ml_training": any(k in lower for k in ["training", "fine-tuning", "loss", "epoch"]),
        "ml_inference": any(k in lower for k in ["inference", "predict", "serving"]),
        "data": any(k in lower for k in ["dataset", "etl", "pipeline"]),
        "production": any(k in lower for k in ["deploy", "docker", "kubernetes", "production"])
    }

PROJECT_TITLE_PATTERN = re.compile(
    r"^(?P<title>.+?)\s+—\s+(?P<role>.+)$",
    re.MULTILINE
)

def split_projects(text: str) -> List[str]:
    matches = list(PROJECT_TITLE_PATTERN.finditer(text))
    blocks = []

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        blocks.append(text[start:end].strip())

    return blocks

# Trích xuất thông tin project từ block text
def extract_project(block: str) -> Optional[Project]:
    lines = block.splitlines()
    if not lines:
        return None

    m = PROJECT_TITLE_PATTERN.match(lines[0])
    if not m:
        return None

    title = m.group("title").strip()
    role = m.group("role").strip()

    # Remove title line
    body = "\n".join(lines[1:])

    # Technologies
    techs = re.search(
        r"Technologies?:\s*(.+)",
        body,
        flags=re.IGNORECASE
    )
    technologies = []
    if techs:
        technologies = [
            t.strip()
            for t in re.split(r",|\|", techs.group(1))
        ]

    # Description = everything except Technologies / Project Link
    description = re.sub(
        r"(Technologies?:.*|Project Link:.*)",
        "",
        body,
        flags=re.IGNORECASE
    ).strip()

    return Project(
        title=title,
        role=role,
        description=description,
        technologies=technologies,
        signals=infer_project_signals(block)
    )

# Trích xuất thông tin từ các section đã cấu trúc và chuyển thành định dạng có cấu trúc json
def extract_from_sections(sections: Dict[str, str]) -> Dict[str, Any]:
    logger.info("Start extraction")

    extracted: Dict[str, Any] = {}

    # Skills
    if "skills" in sections:
        extracted["skills"] = asdict(
            extract_skills(sections["skills"])
        )
        
    # Tools
    if "tools" in sections:
        extracted["tools"] = extract_tools(sections["tools"])

    # Certifications
    if "certifications" in sections:
        extracted["certifications"] = [
            asdict(c)
            for c in extract_certifications(sections["certifications"])
        ]

    # Projects
    projects = []
    if "projects" in sections:
        for block in split_projects(sections["projects"]):
            p = extract_project(block)
            if p:
                projects.append(asdict(p))


    extracted["projects"] = projects
    
    LOG_DIR = Path(__file__).resolve().parents[2] / "logs" / "resume" / "extracted"

    file_path = dump_json(
        extracted,
        base_dir=LOG_DIR,
        prefix="extracted"
    )

    logger.info("Extraction result saved to %s", file_path)
    
    logger.info("Extraction completed")
    
    return extracted

