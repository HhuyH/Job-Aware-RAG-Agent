# File này trích xuất dữ liệu có cấu trúc từ từng section CV (identity, skills, tools, projects, work experience, certifications…) 
# bằng regex + heuristic, chuyển text đã structure thành excel chuẩn để downstream dùng trực tiếp.

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from common.logger import get_logger
from common.json_logger import dump_json
from pathlib import Path
import pandas as pd
import unicodedata
import json
import re


logger = get_logger("agent.resume.extraction")

# Data Classes
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
    
@dataclass
class Identity:
    name: str
    role: str
from typing import List, Optional
from dataclasses import dataclass
import re

@dataclass
class WorkExperience:
    company: str
    role: str
    start_date: Optional[str]
    end_date: Optional[str]
    description: str

# ---------- Các hàm xử lý các section ----------

ROLE_KEYWORDS = ["engineer", "intern", "junior", "fresher", "developer", "ai", "ml"]

def extract_identity(identity_text: str) -> Identity:
    lines = [line.strip() for line in identity_text.splitlines() if line.strip()]
    if not lines:
        return Identity(name="", role="")

    name = ""
    role = ""

    if len(lines) == 1:
        name = lines[0]
    elif len(lines) >= 2:
        for i, line in enumerate(lines):
            if any(k.lower() in line.lower() for k in ROLE_KEYWORDS):
                role = line
                name = lines[0] if i != 0 else lines[1]
                break
        else:
            # fallback mặc định
            name, role = lines[0], lines[1]

    return Identity(name=name, role=role)

# Extractor Functions
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

# Extract Tools
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
        pattern = r"\b" + re.escape(tool) + r"\b"
        if re.search(pattern, lower_text):
            name = tool
            if tool in ("vscode", "vs code"):
                name = "VS Code"
            elif tool == "ssms":
                name = "SQL Server Management Studio"
            else:
                name = tool.title()
            found.add(name)

    return [{"name": t} for t in sorted(found)]

# Extract Certifications
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

# Trích xuất tín hiệu project và những gì đuoc
PROJECT_SIGNAL_KEYWORDS = {
    "llm": ["llm", "gpt", "rag", "langchain"],
    "backend": ["api", "fastapi", "flask", "backend"],
    "ml_training": ["training", "fine-tuning", "loss", "epoch"],
    "ml_inference": ["inference", "predict", "serving"],
    "data": ["dataset", "etl", "pipeline"],
    "production": ["deploy", "docker", "kubernetes", "production"]
}

def infer_project_signals(text: str) -> dict:
    text = text.lower()
    signals = {}
    for signal, keywords in PROJECT_SIGNAL_KEYWORDS.items():
        signals[signal] = any(re.search(rf"\b{k}\b", text) for k in keywords)
    return signals

PROJECT_TITLE_PATTERN = re.compile(
    r"^(?P<title>.+?)\s+—\s+(?P<role>.+)$",
    re.MULTILINE
)

# Tách project blocks
def split_projects(text: str) -> List[str]:
    matches = list(PROJECT_TITLE_PATTERN.finditer(text))
    blocks = []

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        blocks.append(text[start:end].strip())

    return blocks

# trích xuất project từ block
def extract_project(block: str) -> Optional[Project]:
    lines = block.splitlines()
    if not lines:
        return None

    m = PROJECT_TITLE_PATTERN.match(lines[0])
    if not m:
        return None

    title = m.group("title").strip()
    role = m.group("role").strip()
    body = "\n".join(lines[1:])

    techs = re.search(r"Technologies?:\s*(.+)", body, flags=re.IGNORECASE)
    technologies = []
    if techs:
        technologies = [t.strip() for t in re.split(r",|\|", techs.group(1))]

    description = re.sub(r"(Technologies?:.*|Project Link:.*)", "", body, flags=re.IGNORECASE).strip()

    return Project(
        title=title,
        role=role,
        description=description,
        technologies=technologies,
        signals=infer_project_signals(block)
    )

# Regex patterns để detect title + duration
WORK_TITLE_PATTERN = re.compile(
    r"""
    ^(?P<company>.+?)\s*[-–—@]\s*(?P<role>.+)$   # Company — Role hoặc Role @ Company
    """,
    re.MULTILINE | re.VERBOSE
)

DURATION_PATTERN = re.compile(
    r"(?P<start>[A-Za-z]{3,9} \d{4})\s*[-–to]+\s*(?P<end>[A-Za-z]{3,9} \d{4}|Present)",
    re.IGNORECASE
)

def extract_work_experience(text: str) -> List[WorkExperience]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    experiences = []
    
    matches = list(WORK_TITLE_PATTERN.finditer(text))
    for i, m in enumerate(matches):
        start_idx = m.start()
        end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start_idx:end_idx].strip()
        
        company = m.group("company").strip()
        role = m.group("role").strip()
        start_date = None
        end_date = None
        
        # Tìm duration trong block
        dur_match = DURATION_PATTERN.search(block)
        if dur_match:
            start_date = dur_match.group("start")
            end_date = dur_match.group("end")
        
        # Lấy description (bỏ title + duration nếu có)
        description_lines = []
        for line in block.splitlines()[1:]:
            if not DURATION_PATTERN.search(line):
                description_lines.append(line)
        description = "\n".join(description_lines).strip()
        
        experiences.append(
            WorkExperience(
                company=company,
                role=role,
                start_date=start_date,
                end_date=end_date,
                description=description
            )
        )
    
    return experiences

# ---------- Các hàm xữ lý chung ----------

# Xữ lý tên file excel bằng cách loại bỏ dấu và ký tự đặc biệt ở tên của người trong CV
def slugify_name(name: str) -> str:
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    name = re.sub(r"[^\w]", "_", name)
    return name.upper()

# Map role chính dựa trên skills + project signals hiện tại chỉ giới hạn ở AI/ML/backend
def map_role(structured: Dict[str, Any]) -> str:
    skills = structured.get("skills", {})
    projects = structured.get("projects", [])

    role = "Fresher / Unknown"

    total_signals = {
        "llm": 0,
        "backend": 0,
        "ml_training": 0,
        "ml_inference": 0,
    }

    for p in projects:
        for k in total_signals:
            if p.get("signals", {}).get(k):
                total_signals[k] += 1

    ml_skills = [s["name"].lower() for s in skills.get("ml", [])]

    if (
        "machine learning" in ml_skills
        or "deep learning" in ml_skills
        or total_signals["ml_training"] > 0
    ):
        role = "ML Engineer"
    elif total_signals["backend"] > 0:
        role = "Backend Engineer"
    elif total_signals["llm"] > 0:
        role = "AI / LLM Engineer"

    structured["mapped_role"] = role
    return role

# Lưu dữ liệu đã chuẩn hóa ra file Excel
def save_to_excel(structured: Dict[str, Any], excel_path: Path | None = None) -> Path:
    identity = structured.get("identity", {})
    name = identity.get("name", "UNKNOWN")

    if excel_path is None:
        excel_path = Path("data") / f"{slugify_name(name)}.xlsx"

    excel_path.parent.mkdir(exist_ok=True)

    # Projects
    projects_data = []
    for p in structured.get("projects", []):
        row = {
            "Project": p.get("title"),
            "Role": p.get("role"),
            "Mapped Role": structured.get("mapped_role"),
            "Description": p.get("description"),
            "Technologies": ", ".join(p.get("technologies", [])),
        }
        for sig in ["llm", "backend", "ml_training", "ml_inference", "data", "production"]:
            row[sig] = p.get("signals", {}).get(sig, False)
        projects_data.append(row)

    df_projects = pd.DataFrame(projects_data)

    # Skills
    skills_data = []
    for category, items in structured.get("skills", {}).items():
        for s in items:
            skills_data.append({
                "Category": category,
                "Skill": s.get("name"),
                "Level": s.get("level"),
            })

    df_skills = pd.DataFrame(skills_data)

    # Certifications
    df_certs = pd.DataFrame(structured.get("certifications", []))

    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df_projects.to_excel(writer, sheet_name="projects", index=False)
        df_skills.to_excel(writer, sheet_name="skills", index=False)
        df_certs.to_excel(writer, sheet_name="certifications", index=False)

    return excel_path

# Section Mapping
SECTION_EXTRACTORS = {
    "identity": lambda text: asdict(extract_identity(text)),
    "skills": lambda text: asdict(extract_skills(text)),
    "tools": extract_tools,
    "certifications": lambda text: [asdict(c) for c in extract_certifications(text)],
    "projects": lambda text: [asdict(p) for p in map(extract_project, split_projects(text)) if p],
    "work experience": lambda text: [asdict(w) for w in extract_work_experience(text)],
    # có thể thêm section mới dễ dàng
}

# Main Extraction Function
def extract_from_sections(sections: Dict[str, str]) -> Dict[str, Any]:
    logger.info("Start extraction")

    extracted: Dict[str, Any] = {}

    for section, text in sections.items():
        extractor = SECTION_EXTRACTORS.get(section.lower())
        if extractor:
            extracted[section.lower()] = extractor(text)

    map_role(extracted)
    save_to_excel(extracted)

    logger.info("Extraction completed & saved to Excel")
    return extracted


