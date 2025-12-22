from agent.Agent_JobCollection.adapters.topcv import TopCVAdapter
from agent.Agent_JobCollection.schema.search_intent import SearchIntent
from agent.Agent_JobCollection.normalizer.job_normalizer import JobNormalizer
from agent.Agent_JobCollection.job_saver import save_jobs
from common.logger import get_logger

logger = get_logger("agent.job.test")

# Hàm in kết quả
def print_job(job, idx):
    print(f"\n{'='*20} Job {idx} {'='*20}")
    print(f"Canonical title : {job.canonical_title}")
    
    print("\nSkills:")
    for s in job.skills:
        print(f"  - {s}")

    print("\nExperience:")
    if job.experience:
        for k, v in job.experience.items():
            print(f"  {k}: {v}")
    else:
        print("  None")

    print("\nLocations:")
    if job.location:
        for loc in job.location:
            print(f"  - City      : {loc.get('city')}")
            print(f"    District  : {loc.get('district')}")
            print(f"    Ward      : {loc.get('ward')}")
            print(f"    Street    : {loc.get('street')}")
            print(f"    Type      : {loc.get('type')}")
            print(f"    Confidence: {loc.get('confidence')}")
    else:
        print("  None")

if __name__ == "__main__":

    intent = SearchIntent(
        target_roles=["AI Engineer"],
        keywords=["Python", "Machine Learning"],
        exclude_keywords=["QA", "Tester"],
        seniority="junior",
        locations=["Ho Chi Minh"],
        limit=2
    )

    adapter = TopCVAdapter()
    raw_jobs = adapter.search(intent)

    normalizer = JobNormalizer()

    for i, raw_job in enumerate(raw_jobs, 1):
        normalized = normalizer.normalize(raw_job)
        print_job(normalized, i)
        
    normalized_jobs = [normalizer.normalize(rj) for rj in raw_jobs]

    # Lưu thông tin job vào file excel và json
    save_jobs(normalized_jobs)