from agent.Agent_JobCollection.adapters.topcv import TopCVAdapter
from agent.Agent_JobCollection.schema.search_intent import SearchIntent
from agent.Agent_JobCollection.normalizer.job_normalizer import JobNormalizer
from common.logger import get_logger

logger = get_logger("agent.job.test")

if __name__ == "__main__":

    intent = SearchIntent(
        target_roles=["AI Engineer"],
        keywords=["Python", "Machine Learning"],
        exclude_keywords=["QA", "Tester"],
        seniority="junior",
        locations=["Ho Chi Minh"],
        limit=1
    )

    adapter = TopCVAdapter()
    raw_jobs = adapter.search(intent)

    normalizer = JobNormalizer()

    for i, raw_job in enumerate(raw_jobs, 1):
        normalized = normalizer.normalize(raw_job)

        print(f"\n--- Job {i} ---")
        print("Canonical title:", normalized.canonical_title)
        print("Skills:", normalized.skills)
        print("Experience:", normalized.experience)
        print("Location:", normalized.location)
