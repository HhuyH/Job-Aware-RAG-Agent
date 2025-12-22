import os
import json
import pandas as pd
from common.logger import get_logger

logger = get_logger("agent.job.saver")

def job_to_dict(job):
    """Chuyển NormalizedJob -> dict để lưu JSON/Excel"""
    return {
        "title": job.title,
        "canonical_title": job.canonical_title,
        "company": job.company,
        "description": job.description,
        "cleaned_text": job.cleaned_text,
        "skills": job.skills,
        "experience": job.experience,
        "location": job.location,
        "source_url": job.raw_ref,
        "debug": job.debug,
    }

def save_jobs(jobs,
              json_path=os.path.join("data", "jobs", "normalized_jobs.json"),
              excel_path=os.path.join("data", "jobs", "normalized_jobs.xlsx")):

    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    os.makedirs(os.path.dirname(excel_path), exist_ok=True)

    dicts = [job_to_dict(j) for j in jobs]

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(dicts, f, ensure_ascii=False, indent=2)

    df = pd.DataFrame(dicts)
    df.to_excel(excel_path, index=False)

    logger.info(f"Saved {len(jobs)} jobs to {json_path} and {excel_path}")
