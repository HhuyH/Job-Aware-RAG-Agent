# tách cấu trúc CV thành các section dựa trên heading và nội dung

from typing import Dict, List
import re

from common.logger import get_logger

logger = get_logger("agent.resume.structuring")

# Map từ keywords trong heading -> section semantic
SECTION_HEADINGS = {
    "education": ["education", "academic"],
    "experience": ["experience", "employment"],
    "projects": ["project"],
    "skills": ["skill", "technology", ],
    "tools": ["tool", "platform", "environment"],
    "certifications": ["certification", "certificate"],
}


META_HEADINGS = [
    "about",
    "profile",
    "summary",
    "career objective",
    "objective",
    "professional summary"
]

# Heuristic xác định 1 dòng có phải heading hay không
def is_heading(line: str) -> bool:
    words = line.split()

    if len(words) > 5:
        return False

    if line.isupper():
        return True

    if line.istitle():
        return True

    return False

# Map dòng heading -> section semantic
def classify_heading(line: str) -> str | None:
    lower = line.lower()

    for sec, keywords in SECTION_HEADINGS.items():
        for k in keywords:
            if k in lower:
                return sec

    for meta in META_HEADINGS:
        if meta in lower:
            return "meta"

    return None

# Chia text thành các block dựa trên dòng trống và dấu hiệu heading
def split_blocks(text: str) -> List[str]:
    PROJECT_TITLE_PATTERN = re.compile(
        r".+—\s*(personal project|project|ai developer|backend developer)",
        re.IGNORECASE
    )
    
    blocks = []
    current = []

    for line in text.split("\n"):
        if not line.strip():
            if current:
                blocks.append("\n".join(current))
                current = []
            continue
        
        # sử dụng Title Case để nhận diện tiêu đề project và tách block
        if PROJECT_TITLE_PATTERN.match(line) and current:
            blocks.append("\n".join(current))
            current = [line]
            continue

        # heuristic: dòng kết thúc bằng ":" thường mở block mới
        if line.endswith(":") and current:
            blocks.append("\n".join(current))
            current = [line]
        else:
            current.append(line)

    if current:
        blocks.append("\n".join(current))

    return blocks

# Dự đoán section của block dựa trên nội dung
def infer_block_section(block: str) -> str | None:
    lower = block.lower()

    # Project
    if any(k in lower for k in ["— personal project", "— project", "built", "prototype", "rag system"]):
        return "projects"

    # Experience
    if any(k in lower for k in ["developed", "worked on", "responsible for"]):
        return "experience"

    # Certifications (weakest, usually single-line)
    if any(k in lower for k in ["toeic", "ielts", "certificate"]):
        return "certifications"

    return None


def is_valid_cert(block: str) -> bool:
    # Kiểm tra block có phải là chứng chỉ hay không
    CERT_KEYWORDS = [
        "toeic", "ielts", "certificate", "certification", "coursera",
        "udemy", "google", "aws", "microsoft"
    ]

    # Các từ khóa không hợp lệ trong block chứng chỉ
    CERT_FORBIDDEN = [
        "project", "system", "built", "prototype",
        "implementation", "technology", "technologies",
        "rag", "cnn", "model", "api"
    ]

    lower = block.lower()
    lines = block.splitlines()

    # 1. phải có từ khóa chứng chỉ
    if not any(k in lower for k in CERT_KEYWORDS):
        return False

    # 2. phải ngắn (dưới 3 dòng)
    if len(lines) > 3:
        return False

    # 3. không có từ khóa không hợp lệ
    if any(k in lower for k in CERT_FORBIDDEN):
        return False

    return True

# Chia cấu trúc CV thành các section dựa trên heading
def structure_cv(text: str) -> Dict[str, str]:
    logger.info("Start structuring CV text")

    if not text or len(text) < 100:
        logger.warning("Text too short to structure")
        return {"raw": text}

    lines: List[str] = [
        l.strip()
        for l in text.split("\n")
        if l.strip()
    ]

    sections: Dict[str, List[str]] = {}
    current_section = "header"
    sections[current_section] = []

    for line in lines:
        if is_heading(line):
            heading_type = classify_heading(line)

            # SECTION HEADING (education, projects, ...)
            if heading_type in SECTION_HEADINGS:
                logger.debug(f"Detected section [{heading_type}] -> {line}")
                current_section = heading_type
                sections.setdefault(current_section, [])
                continue

            # META HEADING (about, summary, objective, ...)
            if heading_type == "meta":
                logger.debug(f"Detected meta section -> {line}")
                current_section = "profile"
                sections.setdefault("profile", [])
                continue

            # Nếu là heading nhưng không map được → bỏ qua, không đổi section

        sections[current_section].append(line)

    structured = {
        sec: "\n".join(content)
        for sec, content in sections.items()
    }

    
    # tách nhỏ và phân loại lại các block
    refined_sections: Dict[str, List[str]] = {}

    for sec, content in structured.items():
        blocks = split_blocks(content)

        # certifications: giữ lại các block hợp lệ, bỏ qua phần mở rộng không cần thiết
        if sec == "certifications":
            kept = []
            for b in blocks:
                if is_valid_cert(b):
                    kept.append(b)
                else:
                    logger.debug("Break certifications on first non-cert block")
                    break  # bỏ qua các block sau đó

            if kept:
                refined_sections["certifications"] = kept
            continue  # skip normal processing

        # NORMAL SECTIONS
        for block in blocks:
            inferred = infer_block_section(block)
            target = inferred if inferred and inferred != sec else sec
            refined_sections.setdefault(target, []).append(block)


    structured = {
        sec: "\n\n".join(blocks)
        for sec, blocks in refined_sections.items()
        if blocks
    }

    # hiện thị log các section đã tách
    logger.debug(f"Structured sections: {list(structured.keys())}")
    for sec, content in structured.items():
        logger.debug(f"\n--- {sec} ---\n{content[:]}...\n")

    return structured

