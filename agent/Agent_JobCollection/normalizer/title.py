import re
from typing import Optional, Dict

def normalize_title_text(title: str) -> str:
    text = title.lower()

    for p in NOISE_PATTERNS:
        text = re.sub(p, "", text)

    text = re.sub(r"\s+", " ", text).strip()
    return text

# Trích kinh nghiệm
def extract_seniority(text: str) -> Optional[str]:
    for level, pattern in SENIORITY_PATTERNS.items():
        if re.search(pattern, text):
            return level
    return None

# Tách token xữ lý những role bị tách ra và tốm gọn mà chưa được có trong patterns như AI/Robotics engineer
# Để chuyển vễ kiểu AI engineer, Robotics engineer
def split_title_tokens(text: str) -> list[str]:
    parts = re.split(r"[\/\&\|\+,]", text)
    return [p.strip() for p in parts if p.strip()]

# Trả về role + kinh nghiệm và độ tư tin theo từ khó
def classify_role(title: str, jd_text: Optional[str] = None) -> Dict:
    combined_text = f"{title}\n{jd_text or ''}".lower()
    norm_title = normalize_title_text(title)

    title_tokens = split_title_tokens(norm_title)
    search_space = " ".join(title_tokens) + "\n" + (jd_text or "").lower()

    matched_roles = []

    for role, patterns in ROLE_PATTERNS.items():
        for p in patterns:
            if re.search(p, search_space):
                matched_roles.append(role)
                break

    # Lấy role ưu tiên dựa theo vị trị xấp sếp trong patterns
    role = None
    for r in ROLE_PRIORITY:
        if r in matched_roles:
            role = r
            break

    seniority = extract_seniority(title.lower())

    # Ước tính mức độ tư tin về role này
    confidence = 0.0
    if role:
        confidence += 0.6
    if seniority:
        confidence += 0.2
    if jd_text:
        confidence += 0.2

    return {
        "role": role,
        "seniority": seniority,
        "normalized_title": norm_title,
        "confidence": round(confidence, 2)
    }

# ---------- PATTERNS ----------
# Cấp bật
SENIORITY_PATTERNS = {
    "intern": r"\b(intern|internship|thực\s*tập|tts)\b",
    "junior": r"\b(junior|jr\.?|fresher|entry)\b",
    "senior": r"\b(senior|sr\.?|lead|principal|expert)\b",
    "mid": r"\b(mid|middle|experienced)\b"
}

# ROLE KEYWORDS (VN + EN)
ROLE_PATTERNS = {
    "AI Engineer": [
        r"\b(ai engineer|engineer ai|kỹ\s*sư\s*ai)\b",
    ],
    "ML Engineer": [
        r"\b(machine learning engineer|ml engineer|kỹ\s*sư\s*học\s*máy)\b",
    ],
    "Data Scientist": [
        r"\b(data scientist|nhà\s*khoa\s*học\s*dữ\s*liệu)\b",
    ],
    "AI Developer": [
        r"\b(ai developer|lập\s*trình\s*viên\s*ai|ai programmer)\b",
    ],
    "NLP Engineer": [
        r"\b(nlp engineer|xử\s*lý\s*ngôn\s*ngữ)\b",
    ],
    "Computer Vision Engineer": [
        r"\b(computer vision|cv engineer|thị\s*giác\s*máy\s*tính)\b",
    ],
    "LLM Engineer": [
        r"\b(llm|large language model|generative ai)\b",
    ],
    "Robotics Engineer": [
        r"\b(robotics engineer|robot engineer|kỹ\s*sư\s*robot)\b",
    ],
}

# Trả về những role ưu tiên để tránh bỏ sót role
ROLE_PRIORITY = [
    "Robotics Engineer",
    "LLM Engineer",
    "NLP Engineer",
    "Computer Vision Engineer",
    "ML Engineer",
    "AI Engineer",
    "AI Developer",
    "Data Scientist",
]

# CLEAN TITLE
NOISE_PATTERNS = [
    r"\[.*?\]",
    r"\(.*?\)",
    r"tuyển\s*gấp",
    r"urgent",
    r"hot job",
    r"lương\s*cao",
    r"remote",
    r"hybrid",
    r"full[-\s]?time",
    r"part[-\s]?time",
    r"onsite",
    r"tại\s*.*$",
]
