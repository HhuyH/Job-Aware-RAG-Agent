from dataclasses import dataclass, field
from typing import Optional, List, Union ,Dict
from .source_meta import SourceMeta


@dataclass
class RawJob:
    # -------- Thông tin cơ bản --------
    title: str
    company: str
    description: str

    # -------- Metadata nguồn --------
    source: SourceMeta

    # -------- Thông tin bổ sung --------
    location: Optional[str] = None
    salary: Optional[str] = None
    employment_type: Optional[str] = None  # full-time, intern, contract

    # -------- Tín hiệu trích xuất thô --------
    extracted_keywords: List[str] = field(default_factory=list)

    # Yêu cầu kinh nghiệm (structured, KHÔNG suy luận)
    experience: Optional[Dict[str, Optional[float]]] = None
    # format:
    # {
    #   "min_years": float | None,
    #   "max_years": float | None,
    #   "raw_text": str | None
    # }

    # -------- Debug / Trace --------
    extra: dict = field(default_factory=dict)
