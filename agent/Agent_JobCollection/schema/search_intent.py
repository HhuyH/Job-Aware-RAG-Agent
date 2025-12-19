from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class SearchIntent:
    # Vai trò mục tiêu
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
