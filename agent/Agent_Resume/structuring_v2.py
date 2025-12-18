# V2 chia CV thành section rõ hơn, xử lý dòng dài và chứng chỉ riêng, dùng chiến lược consume & remove, 
# giảm trùng lặp, trong khi V1 chỉ tách block dựa trên heading và keyword mà chưa tối ưu dòng dài hay merge duplicate.

from typing import Dict, List, Tuple
import re
from common.logger import get_logger

logger = get_logger("agent.resume.structuring")


# CONFIG
SECTION_HEADINGS = {
    "education": ["education", "academic"],
    "experience": ["experience", "employment"],
    "projects": ["project"],
    "skills": ["skill", "technology"],
    "tools": ["tool", "platform", "environment"],
    "certifications": ["certification", "certificate"],
}

META_HEADINGS = [
    "about",
    "profile",
    "summary",
    "career objective",
    "objective",
    "professional summary",
]

ALL_HEADINGS = {
    **SECTION_HEADINGS,
    "profile": META_HEADINGS,
}

CERT_KEYWORDS = [
    "toeic", "ielts", "certificate", "certification",
    "coursera", "udemy", "google", "aws", "microsoft"
]


# kiểm tra dòng có phải heading hay không
def is_heading(line: str) -> bool:
    words = line.split()
    if len(words) > 6:
        return False
    return line.isupper() or line.istitle()

# phân loại heading thành section semantic
def classify_heading(line: str) -> str | None:
    lower = line.lower()
    for sec, keys in ALL_HEADINGS.items():
        for k in keys:
            if k in lower:
                return sec
    return None

# chia dòng dài thành các phần nhỏ hơn nếu cần
def split_long_line_dynamic(line: str, min_gap: int = 15) -> List[str]:
    words = [(m.start(), m.group()) for m in re.finditer(r'\S+', line)]
    if not words:
        return [line.strip()]
    split_indices = []
    for i in range(len(words) - 1):
        gap = words[i + 1][0] - (words[i][0] + len(words[i][1]))
        if gap >= min_gap:
            split_indices.append(i + 1)
    if not split_indices:
        return [line.strip()]
    columns = []
    prev_idx = 0
    for idx in split_indices:
        columns.append(" ".join(w[1] for w in words[prev_idx:idx]).strip())
        prev_idx = idx
    columns.append(" ".join(w[1] for w in words[prev_idx:]).strip())
    return [c for c in columns if c]

# trích xuất section từ dòng heading đến heading tiếp theo
def extract_section(lines: List[str], start_idx: int) -> Tuple[str, List[str], int]:
    heading_line = lines[start_idx]
    section_name = classify_heading(heading_line)
    content: List[str] = []
    i = start_idx + 1
    while i < len(lines):
        if is_heading(lines[i]) and classify_heading(lines[i]):
            break
        content.append(lines[i])
        i += 1
    return section_name, content, i

# tách dòng chứng chỉ khỏi các dòng không xác định
def split_cert_and_unresolved(sec_lines: List[str]) -> Tuple[List[str], List[str]]:
    cert_lines = []
    unresolved_lines = []
    for line in sec_lines:
        lower = line.lower()
        if any(k in lower for k in CERT_KEYWORDS) and len(line.split()) < 15:
            cert_lines.append(line)
        else:
            unresolved_lines.append(line)
    return cert_lines, unresolved_lines

# chính hàm cấu trúc CV
def structure_cv(text: str) -> Dict[str, str]:
    logger.info("Start CV structuring (consume & remove strategy)")

    if not text or len(text) < 100:
        logger.warning("Text too short")
        return {"raw": text}

    # Split lines and pre-process long lines
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    text_pool: List[str] = []
    for l in lines:
        text_pool.extend(split_long_line_dynamic(l))

    structured: Dict[str, List[str]] = {}
    unresolved: List[str] = []

    i = 0
    while i < len(text_pool):
        line = text_pool[i]

        if is_heading(line):
            sec_name, sec_lines, end_idx = None, [], i
            sec = classify_heading(line)
            if sec:
                logger.debug(f"Detected heading [{sec}] -> {line}")
                sec_name, sec_lines, end_idx = extract_section(text_pool, i)

                if sec_name in ["projects", "unresolved", "certifications"]:
                    cert_lines, non_cert_lines = split_cert_and_unresolved(sec_lines)
                    if cert_lines:
                        structured.setdefault("certifications", []).extend(cert_lines)
                    if non_cert_lines:
                        structured.setdefault("unresolved", []).extend(non_cert_lines)
                else:
                    structured.setdefault(sec_name, []).extend(sec_lines)

                # Remove consumed lines
                del text_pool[i:end_idx]
                continue  # stay at same index after deletion

        # Non-heading lines: move to unresolved temporarily
        unresolved.append(line)
        i += 1

    # Any remaining lines in text_pool (sau loop) cũng đưa vào unresolved
    unresolved.extend(text_pool)

    # Merge unresolved
    if unresolved:
        structured.setdefault("unresolved", []).extend(unresolved)

    # Convert lists -> strings
    result: Dict[str, str] = {
        sec: "\n".join(content).strip()
        for sec, content in structured.items()
        if content
    }

    # Remove duplicate lines in all sections
    for sec, content in result.items():
        lines = content.split("\n")
        unique_lines = []
        seen = set()
        for l in lines:
            if l not in seen:
                unique_lines.append(l)
                seen.add(l)
        result[sec] = "\n".join(unique_lines)

    logger.debug("Structured sections: %s", list(result.keys()))
    for sec, content in result.items():
        logger.debug(f"\n--- {sec.upper()} ---\n{content[:500]}\n")

    
    return result
