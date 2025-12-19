from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class SourceMeta:
    platform: str               # linkedin / topcv / itviec / fb / google
    url: Optional[str]
    collected_at: datetime
    raw_id: Optional[str] = None  # id gốc từ platform nếu có
