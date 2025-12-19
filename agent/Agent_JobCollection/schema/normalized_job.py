from dataclasses import dataclass, field
from typing import Optional, List, Dict
from .source_meta import SourceMeta


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
