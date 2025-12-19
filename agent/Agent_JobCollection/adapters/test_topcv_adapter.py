from .topcv import TopCVAdapter
from agent.Agent_JobCollection.schema.search_intent import SearchIntent
from common.logger import get_logger

logger = get_logger("agent.resume.structuring")

def main():
    intent = SearchIntent(
        target_roles=["AI Engineer"],
        keywords=["Python", "Machine Learning"],
        exclude_keywords=["QA", "Tester"],
        seniority="junior",
        locations=["Ho Chi Minh"],
        limit=1
    )

    adapter = TopCVAdapter()
    jobs = adapter.search(intent)
    
    print(f"Collected {len(jobs)} jobs\n")
    
    for i, job in enumerate(jobs, 1):

        print(f"--- Job {i} ---")
        print("Title   :", job.title)
        print("Company :", job.company)
        print("Location:", job.location)
        print("Source  :", job.source.platform)
        print("URL     :", job.source.url)
        print("Keywords:", job.extracted_keywords)
        print()

if __name__ == "__main__":
    main()
