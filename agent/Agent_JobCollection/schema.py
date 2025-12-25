from dataclasses import dataclass, field
from typing import Optional, List, Dict, Union
from datetime import datetime

@dataclass
class SearchIntent:
    # Vai trò mục tiêu muốn tìm
    target_roles: List[str]

    # Keyword kỹ thuật chính để search
    keywords: List[str]

    # Keyword cần loại bỏ (QA, Tester, Sales…)
    exclude_keywords: List[str] = field(default_factory=list)

    # Cấp độ (intern / junior / mid / senior)
    seniority: Optional[str] = None

    # Địa điểm mong muốn
    locations: List[str] = field(default_factory=list)

    # Remote / Hybrid / Onsite
    work_modes: List[str] = field(default_factory=list)

    # Ngành/domain ưu tiên (chatbot, fintech, healthcare…)
    domains: List[str] = field(default_factory=list)
    
    # Địa điểm ưu tiên
    locations: List[str] = field(default_factory=list)

    # Giới hạn số job cần lấy (soft limit)
    limit: int = 100

@dataclass
class SourceMeta:
    platform: str               # linkedin / topcv / itviec / fb / google
    url: Optional[str]
    collected_at: datetime
    raw_id: Optional[str] = None  # id gốc từ platform nếu có

@dataclass
class RawJob:
    # Thông tin cơ bản
    title: str
    company: str
    description: str

    # Metadata nguồn
    source: SourceMeta

    # Thông tin bổ sung
    location: Optional[str] = None
    salary: Optional[str] = None
    employment_type: Optional[str] = None  # full-time, intern, contract

    # Tín hiệu trích xuất thô
    extracted_keywords: List[str] = field(default_factory=list)

    # Yêu cầu kinh nghiệm (structured, KHÔNG suy luận)
    experience: Optional[Dict[str, Optional[float]]] = None
    # format:
    # {
    #   "min_years": float | None,
    #   "max_years": float | None,
    #   "raw_text": str | None
    # }

    # Debug / Trace
    extra: dict = field(default_factory=dict)


@dataclass
class NormalizedJob:
    # Identity
    title: str
    canonical_role: Optional[str]
    seniority: Optional[str]

    # Company & source
    company: str
    source: SourceMeta

    # JD
    description: str

    # Location
    location: Optional[str]

    # Experience
    experience: Optional[Dict]

    # Skills
    skills: List[str] = field(default_factory=list)

    # Metadata
    confidence: float = 0.0
    raw: Optional[dict] = None  # giữ RawJob để trace/debug