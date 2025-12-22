# File này trích xuất dữ liệu có cấu trúc từ từng section CV (identity, skills, tools, projects, work experience, certifications…) 
# bằng regex + heuristic, chuyển text đã structure thành excel chuẩn để downstream dùng trực tiếp.

from typing import List, Dict, Any, Optional, Tuple
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
    subskills: Optional[List[str]] = None

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

@dataclass
class WorkExperience:
    company: str
    role: str
    start_date: Optional[str]
    end_date: Optional[str]
    description: str

# ---------- Các hàm xử lý các section ----------
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

# Ghép các dòng multiline cho skill/project trước khi extract.
def preprocess_lines(text: str) -> list[str]:
    lines = text.splitlines()
    new_lines = []
    buffer = ""
    for line in lines:
        line = line.strip()
        if line.startswith("•"):
            if buffer:
                new_lines.append(buffer)
            buffer = line
        else:
            # Nếu dòng trước buffer kết thúc bằng dấu '-', nối tiếp
            if buffer.endswith("-") or len(buffer) < 80:
                buffer += " " + line
            else:
                new_lines.append(buffer)
                buffer = line
    if buffer:
        new_lines.append(buffer)
    return new_lines

# Trích phân loại skills 
def extract_skills(text: str) -> SkillSet:
    skills = { "languages": [], "frameworks": [], "ml": [], "databases": [] }

    def smart_split(text: str) -> Tuple[str, List[str]]:
        """
        Tách main skill và subskills nếu có dấu ngoặc, kể cả khi đóng ngoặc thiếu
        """
        text = text.strip().rstrip(").")  # loại bỏ dấu dư cuối
        # Thử match chuẩn
        m = re.match(r"^(.*?)\s*\((.+)\)$", text)
        if m:
            main_skill = m.group(1).strip()
            subskills = [s.strip() for s in m.group(2).split(",") if s.strip()]
            return main_skill, subskills

        # fallback: tìm '(' nhưng không có ')'
        if "(" in text:
            parts = text.split("(", 1)
            main_skill = parts[0].strip()
            subskills = [s.strip() for s in parts[1].split(",") if s.strip()]
            return main_skill, subskills

        return text, []


    def split_top_level_commas(text: str) -> List[str]:
        """
        Tách text theo dấu phẩy nhưng bỏ qua dấu trong ngoặc
        """
        items = []
        buffer = ""
        depth = 0
        for c in text:
            if c == "(":
                depth += 1
                buffer += c
            elif c == ")":
                depth -= 1
                buffer += c
            elif c == "," and depth == 0:
                items.append(buffer.strip())
                buffer = ""
            else:
                buffer += c
        if buffer:
            items.append(buffer.strip())
        return items

    for section_header, category in SECTION_MAP.items():
        pattern = re.compile(rf"{re.escape(section_header)}\s*:?", re.IGNORECASE)
        match = pattern.search(text)
        if not match:
            continue

        start_idx = match.end()
        next_headers = [h for h in SECTION_MAP.keys() if h.lower() != section_header.lower()]
        end_idx = len(text)
        for nh in next_headers:
            nh_pattern = re.compile(rf"{re.escape(nh)}\s*:?", re.IGNORECASE)
            nh_match = nh_pattern.search(text, pos=start_idx)
            if nh_match:
                end_idx = nh_match.start()
                break

        section_text = text[start_idx:end_idx].strip()
        if not section_text:
            continue

        lines = preprocess_lines(section_text)
        for raw in lines:
            line = raw.strip()
            if not line.startswith("•"):
                continue

            content = line.lstrip("•").strip()
            l = content.lower()

            # xác định level
            if any(k in l for k in ["experience", "proficient", "advanced"]):
                level = "core"
            elif any(k in l for k in ["familiar", "basic"]):
                level = "exposure"
            else:
                level = "core"

            # Normalize
            normalized = False
            for pattern, name in NORMALIZE_MAP.items():
                if re.search(pattern, content, flags=re.IGNORECASE):
                    skills[category].append(SkillItem(name=name, level=level))
                    normalized = True
                    break
            if normalized:
                continue

            # Tách từng item, giữ subskills trong ngoặc
            raw_items = split_top_level_commas(content)
            for item in raw_items:
                main_skill, subskills = smart_split(item)
                skills[category].append(SkillItem(name=main_skill, level=level, subskills=subskills))

    # Dedupe toàn bộ category (giữ subskills union)
    for cat in skills.keys():
        seen = {}
        unique_items = []
        for s in skills[cat]:
            key = (s.name.lower(), s.level)
            if key in seen:
                existing = seen[key]
                if s.subskills:
                    if existing.subskills:
                        existing.subskills = list(set(existing.subskills + s.subskills))
                    else:
                        existing.subskills = s.subskills
            else:
                unique_items.append(s)
                seen[key] = s
        skills[cat] = unique_items

    return SkillSet(**skills)


def is_short_skill_list(line: str) -> bool:
    if any(k in line.lower() for k in [
        "experience", "integrat", "pipeline", "workflow", "system"
    ]):
        return False
    if "(" in line or ")" in line:
        return False
    return "," in line and len(line.split(",")) <= 4

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


def infer_project_signals(text: str) -> dict:
    text = text.lower()
    signals = {}
    for signal, keywords in PROJECT_SIGNAL_KEYWORDS.items():
        signals[signal] = any(re.search(rf"\b{k}\b", text) for k in keywords)
    return signals

# Tách project blocks
def split_projects(text: str) -> List[str]:
    matches = list(PROJECT_TITLE_PATTERN.finditer(text))
    blocks = []

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        blocks.append(text[start:end].strip())

    return blocks

# Trích xuất project từ block
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

# Trích xuất kinh nghiệm
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
        excel_path = Path("data") / "cv" / f"{slugify_name(name)}.xlsx"

    excel_path.parent.mkdir(parents=True, exist_ok=True)

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

# Lưu dữ liệu đã chuẩn hóa ra file Json
def save_to_json(structured: Dict[str, Any], json_path: Path | None = None) -> Path:
    identity = structured.get("identity", {})
    name = identity.get("name", "UNKNOWN")

    if json_path is None:
        json_path = Path("data") / "cv" / f"{slugify_name(name)}.json"

    json_path.parent.mkdir(parents=True, exist_ok=True)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(structured, f, ensure_ascii=False, indent=2)

    return json_path

# Hàm xữ lý chính 
def extract_from_sections(sections: Dict[str, str]) -> Dict[str, Any]:
    logger.info("Start extraction")

    extracted: Dict[str, Any] = {}

    for section, text in sections.items():
        extractor = SECTION_EXTRACTORS.get(section.lower())
        if extractor:
            extracted[section.lower()] = extractor(text)

    map_role(extracted)

    json_path = save_to_json(extracted)
    excel_path = save_to_excel(extracted)

    logger.info(f"Extraction completed")
    logger.info(f"Saved JSON  : {json_path}")
    logger.info(f"Saved Excel : {excel_path}")

    return extracted

# ---------- PATTERNS ----------
# Role keywords
ROLE_KEYWORDS = ["engineer", "intern", "junior", "fresher", "developer", "ai", "ml"]

# Section Mapping
SECTION_EXTRACTORS = {
    "identity": lambda text: asdict(extract_identity(text)),
    "skills": lambda text: asdict(extract_skills(text)),
    "tools": extract_tools,
    "certifications": lambda text: [asdict(c) for c in extract_certifications(text)],
    "projects": lambda text: [asdict(p) for p in map(extract_project, split_projects(text)) if p],
    "work experience": lambda text: [asdict(w) for w in extract_work_experience(text)],
    # có thể thêm section
}

# Regex patterns để detect title + duration
WORK_TITLE_PATTERN = re.compile(
    r"""
    ^(?P<company>.+?)\s*[-–—@]\s*(?P<role>.+)$   # Company — Role hoặc Role @ Company
    """,
    re.MULTILINE | re.VERBOSE
)

SECTION_MAP = {
    "programming languages": "languages",
    "frameworks": "frameworks",
    "frameworks & technologies": "frameworks",
    "ai / machine learning": "ml",
    "database": "databases",
}

LEVEL_HINTS = {
    "exposure": ["familiar", "basic", "exposure"],
}

# Pattern thời gian dự án 
DURATION_PATTERN = re.compile(
    r"(?P<start>[A-Za-z]{3,9} \d{4})\s*[-–to]+\s*(?P<end>[A-Za-z]{3,9} \d{4}|Present)",
    re.IGNORECASE
)

# Trích xuất tín hiệu project và những gì đuoc
PROJECT_SIGNAL_KEYWORDS = {
    "llm": ["llm", "gpt", "rag", "langchain"],
    "backend": ["api", "fastapi", "flask", "backend"],
    "ml_training": ["training", "fine-tuning", "loss", "epoch"],
    "ml_inference": ["inference", "predict", "serving"],
    "data": ["dataset", "etl", "pipeline"],
    "production": ["deploy", "docker", "kubernetes", "production"]
}

# Tiêu đề project tuy nhiên nếu có các dạng phực tập hoặc khác thì khó tách được
PROJECT_TITLE_PATTERN = re.compile(
    r"^(?P<title>.+?)\s+—\s+(?P<role>.+)$",
    re.MULTILINE
)

CERT_PATTERN = re.compile(
    r"""
    (?P<name>TOEIC|IELTS|JLPT|HSK|CEFR)
    [^\d]{0,10}
    (?P<score>\d{2,4})?
    """,
    re.IGNORECASE | re.VERBOSE
)

NORMALIZE_MAP = {
    r"retrieval\s*-\s*augmented generation.*": "RAG",
    r"llm workflow orchestration.*": "LLM Orchestration",
    r"conversational ai.*multi-turn.*": "Conversational AI",
    r"data preprocessing.*": "Data Preprocessing",
    r"model training.*": "Model Training",
    r"experience integrating llm-based.*": "LLM Integration"
}
