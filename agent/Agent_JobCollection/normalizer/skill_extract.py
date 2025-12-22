import re
from typing import List, Dict, Optional


# Danh sách skills
SKILL_PATTERNS: Dict[str, List[str]] = {
    #  Core programming 
    "python": [r"\bpython\b"],
    "java": [r"\bjava\b"],
    "c++": [r"\bc\+\+\b"],
    "sql": [r"\bsql\b"],
    
    #  ML / AI 
    "machine learning": [
        r"machine[\s\-]?learning",
        r"\bml\b"
    ],
    "deep learning": [
        r"deep[\s\-]?learning",
        r"\bdl\b"
    ],
    "artificial intelligence": [
        r"\bartificial intelligence\b",
        r"\bai\b"
    ],

    #  NLP / LLM 
    "nlp": [
        r"\bnlp\b",
        r"natural[\s\-]?language"
    ],
    "llm": [
        r"\bllm\b",
        r"large[\s\-]?language[\s\-]?model"
    ],
    "transformer": [
        r"\btransformer\b",
        r"attention model"
    ],

    #  Frameworks 
    "pytorch": [r"\bpytorch\b"],
    "tensorflow": [r"\btensorflow\b"],
    "keras": [r"\bkeras\b"],
    "scikit-learn": [r"scikit[\s\-]?learn", r"\bsklearn\b"],

    #  Data 
    "pandas": [r"\bpandas\b"],
    "numpy": [r"\bnumpy\b"],
    "spark": [r"\bspark\b"],

    #  MLOps 
    "docker": [r"\bdocker\b"],
    "kubernetes": [r"\bkubernetes\b|\bk8s\b"],
    "mlops": [r"\bmlops\b"],
    "airflow": [r"\bairflow\b"],

    #  Cloud 
    "aws": [r"\baws\b|amazon web services"],
    "gcp": [r"\bgcp\b|google cloud"],
    "azure": [r"\bazure\b"]
}

# Những từ ko cần thiết
NOISE_KEYWORDS = {
    "communication",
    "teamwork",
    "problem solving",
    "critical thinking",
    "fast learner",
    "english",
    "presentation"
}

# Trích xuất kỹ năng từ JD
def extract_skills(
    text: str,
    fallback_keywords: Optional[List[str]] = None
) -> List[str]:

    if not text:
        text = ""

    text = text.lower()
    skills_found = set()

    # trích từ raw JD
    for skill, patterns in SKILL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text):
                skills_found.add(skill)
                break

    # Trả về keywork có trong danh sách
    if fallback_keywords:
        for kw in fallback_keywords:
            kw_norm = kw.lower().strip()
            if kw_norm in SKILL_PATTERNS:
                skills_found.add(kw_norm)

    # Loại bỏ những từ ko cần thiết
    skills_cleaned = [
        s for s in skills_found
        if s not in NOISE_KEYWORDS
    ]

    return sorted(skills_cleaned)
