# agent/Agent_JobCollection/adapters/topcv.py

import requests
from bs4 import BeautifulSoup
from typing import List, Optional, Dict
import re


from agent.Agent_JobCollection.adapters.base import AbstractJobAdapter
from agent.Agent_JobCollection.schema.search_intent import SearchIntent
from agent.Agent_JobCollection.schema.raw_job import RawJob
from common.logger import get_logger

logger = get_logger("agent.resume.structuring")

class TopCVAdapter(AbstractJobAdapter):
    platform_name = "topcv"
    location_forTopCV = "ho-chi-minh"
    location_code = "l2"

    BASE_URL = "https://www.topcv.vn"

    def __init__(self, timeout: int = 10):
        super().__init__()
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept": "text/html,application/xhtml+xml",
            "Referer": "https://www.topcv.vn/"
        })

    #  CORE 
    def search(self, intent: SearchIntent) -> List[RawJob]:
        jobs: List[RawJob] = []

        url = self._build_search_url(intent, location_forTopCV=self.location_forTopCV, location_code=self.location_code)

        resp = self.session.get(url, timeout=self.timeout)
        if resp.status_code != 200:
            return jobs  # không crash agent
        
        logger.info(f"\nSEARCH URL: {url}\nSTATUS: {resp.status_code}\nHTML LEN: {len(resp.text)}")

        soup = BeautifulSoup(resp.text, "html.parser")
        job_cards = soup.select(".job-item-search-result")
        
        logger.info(f"Found {len(job_cards) - 1} job cards on TopCV.")
        
        for card in job_cards:
            job = self._parse_job_card(card)
            if job:
                jobs.append(job)

            if len(jobs) >= intent.limit:
                break

        return jobs

    #  INTERNAL 
    # Xây dựng URL tìm kiếm dựa trên SearchIntent cho TopCV
    def _build_search_url(self, intent: SearchIntent, location_forTopCV: str, location_code: str) -> str:
        role = intent.target_roles[0] if intent.target_roles else "ai engineer"
        role_slug = self._slugify(role)

        return (
            f"{self.BASE_URL}/tim-viec-lam-{role_slug}-tai-{location_forTopCV}-kl2"
            f"?type_keyword=1"
            f"&sba=1"
            f"&locations={location_code}"
            f"&saturday_status=0"
        )

    # Chuyển chuỗi thành slug (dùng cho URL)
    def _slugify(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"\s+", "-", text)
        return text

    # Phân tích thẻ job và trích xuất thông tin thành RawJob
    def _parse_job_card(self, card) -> RawJob | None:
        try:
            title_el = card.select_one("h3.title a")
            company_el = card.select_one(".company-name")
            location_el = card.select_one(".address .city-text")

            if not title_el or not company_el:
                return None

            title = title_el.get_text(strip=True)
            company = company_el.get_text(strip=True)
            location = location_el.get_text(strip=True) if location_el else None
            url = title_el.get("href")

            description = self._fetch_job_detail(url) if url else ""
            
            return RawJob(
                title=title,
                company=company,
                description=description,
                location=location,
                source=self.build_source_meta(url=url),
                extracted_keywords=self._extract_keywords(description)
            )

        except Exception as e:
            print("PARSE ERROR:", e)
            return None

    def _fetch_job_detail(self, url: str) -> str:
        try:
            resp = self.session.get(url, timeout=self.timeout)
            if resp.status_code != 200:
                return ""

            soup = BeautifulSoup(resp.text, "html.parser")
            jd_el = soup.select_one(".job-description")
            return jd_el.get_text("\n", strip=True) if jd_el else ""

        except Exception:
            return ""

    # Trích xuất keywords từ JD 
    def _extract_keywords(self, text: str) -> List[str]:
        if not text:
            return []

        text = text.lower()
        keywords = set()

        patterns = {
            "python": r"python",
            "machine learning": r"machine[\s\-]?learning",
            "deep learning": r"deep[\s\-]?learning",
            "ai": r"\bai\b|ai[\-\/]",
            "nlp": r"nlp|natural language",
            "llm": r"llm|large language model"
        }

        for kw, pattern in patterns.items():
            if re.search(pattern, text):
                keywords.add(kw)

        return list(keywords)
    