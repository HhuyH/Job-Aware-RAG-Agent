from bs4 import BeautifulSoup
from typing import List
import requests
import re

from .base import AbstractJobAdapter
from ..schema import SearchIntent, RawJob

from common.logger import get_logger
logger = get_logger("agent.resume.structuring")

class ItViecAdapter(AbstractJobAdapter):
    # Tên nền tảng
    platform_name = "itviec"
    
    # Vị trí tìm việc
    location_forITViec = "ho-chi-minh-hcm"

    # Đường dẫn mặc định của nền tảng
    BASE_URL = "https://itviec.com/"

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
            "Referer": "https://itviec.com/"
        })


    def search(self, intent: SearchIntent) -> List[RawJob]:
        jobs: List[RawJob] = []

        url = self.build_search_url(intent, location_forITViec=self.location_forITViec)

        resp = self.session.get(url, timeout=self.timeout)
        print(resp.text[:1000])  # xem HTML trả về có job không

        if resp.status_code != 200:
            return jobs  # không crash agent
        
        logger.info(f"\nSEARCH URL: {url}\nSTATUS: {resp.status_code}\nHTML LEN: {len(resp.text)}")

        soup = BeautifulSoup(resp.text, "html.parser")
        job_cards = soup.select("div.ipx-4.ipx-xl-3")

        logger.info(f"Found {len(job_cards) - 1} job cards on ITViec.")
        
        for card in job_cards:
            job = self.parse_job_card(card)
            if job:
                jobs.append(job)

            if len(jobs) >= intent.limit:
                break

        return jobs

    # Xây dựng URL tìm kiếm dựa trên SearchIntent cho ITViec
    def build_search_url(self, intent: SearchIntent, location_forITViec: str) -> str:
        role = intent.target_roles[0] if intent.target_roles else "ai engineer"
        role_slug = self.slugify(role)

        return (
            f"{self.BASE_URL}/it-jobs/{location_forITViec}?job_selected={role_slug}"
        )

    # Chuyển chuỗi thành slug (dùng cho URL)
    def slugify(self, text: str) -> str:
        text = text.lower() # Ai Engineer -> ai engineer
        
        # ^ ở đầu trong nhóm = phủ định (not).
        # → [^\w\s-] = mọi ký tự không phải…
        # \w = chữ cái, số, gạch dưới [a-zA-Z0-9_].
        # \s = khoảng trắng (space, tab, newline).
        # - = dấu gạch ngang.
        text = re.sub(r"[^\w\s-]", "", text) # Mọi ký tự không phải chữ/số/khoảng trắng/gạch ngang sẽ bị thay thế bằng chuổi rỗng ""
        
        text = re.sub(r"\s+", "-", text) # ai engineer -> ai-engineer
        return text

    # Phân tích thẻ job và trích xuất thông tin thành RawJob
    def parse_job_card(self, card) -> RawJob | None:
        try:
            title_el = card.select_one('h3[data-search--job-selection-target="jobTitle"]')
            company_el = card.select_one("a.text-rich-grey")
            location_el = card.select_one(".text-rich-grey.text-truncate.text-nowrap.stretched-link.position-relative")
                
            if not title_el or not company_el:
                return None

            title = title_el.get_text(strip=True)
            company = company_el.get_text(strip=True)
            location = location_el.get_text(strip=True) if location_el else None
            url = title_el.get("data-url")

            description = self.fetch_job_detail(url) if url else ""
            
            return RawJob(
                title=title,
                company=company,
                description=description,
                location=location,
                source=self.build_source_meta(url=url),
                extracted_keywords=self.extract_keywords(description)
            )

        except Exception as e:
            print("PARSE ERROR:", e)
            return None

    def fetch_job_detail(self, url: str) -> str:
        try:
            resp = self.session.get(url, timeout=self.timeout)
            if resp.status_code != 200:
                return ""

            soup = BeautifulSoup(resp.text, "html.parser")
            wrapper = soup.select_one("div.preview-job-wrapper")
            return str(wrapper) if wrapper else ""

        except Exception:
            return ""

    # Trích xuất keywords từ JD 
    def extract_keywords(self, text: str) -> List[str]:
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
    