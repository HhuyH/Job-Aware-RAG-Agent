from typing import Optional, Dict
from dataclasses import dataclass, field

from agent.Agent_JobCollection.schema.raw_job import RawJob
from agent.Agent_JobCollection.schema.source_meta import SourceMeta

from .title import classify_role
from .jd_text import clean_jd_text
from .skill_extract import extract_skills
from .experience import extract_experience
from .location import normalize_location
from common.logger import get_logger

logger = get_logger("agent.resume.structuring")

# OUTPUT SCHEMA
@dataclass
class NormalizedJob:
    # Core identity
    title: str
    canonical_title: str
    company: str

    # Content
    description: str
    cleaned_text: str

    # Signals
    skills: list = field(default_factory=list)
    experience: Optional[Dict] = None
    location: Optional[Dict] = None

    # Meta
    source: Optional[SourceMeta] = None
    raw_ref: Optional[str] = None  # job id / url
    debug: dict = field(default_factory=dict)


LOCATION_ANCHORS = [
    "địa điểm làm việc",
    "work location",
    "location",
]

STOP_ANCHORS = [
    "thời gian",
    "cách thức",
    "quyền lợi",
    "yêu cầu",
]

def extract_location_block(jd_text: str) -> Optional[str]:
    lines = [l.strip() for l in jd_text.splitlines() if l.strip()]
    buf = []
    capturing = False

    for line in lines:
        line_lc = line.lower()

        if any(a in line_lc for a in LOCATION_ANCHORS):
            capturing = True
            continue

        if capturing:
            if any(s in line_lc for s in STOP_ANCHORS):
                break
            buf.append(line)

    return "\n".join(buf) if buf else None

# NORMALIZER
class JobNormalizer:
    """
    Normalize RawJob → NormalizedJob
    """

    def normalize(self, raw_job: RawJob) -> NormalizedJob:
        # 1. Title
        canonical_title = classify_role(raw_job.title)

        # 2. JD text
        cleaned_text = clean_jd_text(raw_job.description)
        
        # logger.info(f"{raw_job.description}")
        
        # 3. Skills
        skills = extract_skills(cleaned_text)

        # 4. Experience
        experience = extract_experience(cleaned_text)

        # 5. Location
        location_block = extract_location_block(cleaned_text)
        if location_block:
            location_text = location_block.replace("\n", " ")
            location = normalize_location(location_text)
        else:
            location = None

        # print(location_block)
        
        return NormalizedJob(
            title=raw_job.title,
            canonical_title=canonical_title,
            company=raw_job.company,
            description=raw_job.description,
            cleaned_text=cleaned_text,
            skills=skills,
            experience=experience,
            location=location,
            source=raw_job.source,
            raw_ref=raw_job.source.url if raw_job.source else None,
            debug={
                "raw_title": raw_job.title,
                "raw_location": raw_job.location,
                "extracted_keywords": raw_job.extracted_keywords,
            }
        )

