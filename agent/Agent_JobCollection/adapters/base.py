# agent/Agent_JobCollection/adapters/base.py

from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

from agent.Agent_JobCollection.schema.search_intent import SearchIntent
from agent.Agent_JobCollection.schema.raw_job import RawJob
from agent.Agent_JobCollection.schema.source_meta import SourceMeta


class AbstractJobAdapter(ABC):
    """
    Base class cho tất cả Job Adapters.
    Mỗi platform (LinkedIn, TopCV, FB...) phải implement class này.
    """

    #: Tên platform, ví dụ: 'linkedin', 'topcv', 'itviec'
    platform_name: str = "unknown"

    def __init__(self):
        if self.platform_name == "unknown":
            raise ValueError(
                f"{self.__class__.__name__} phải khai báo platform_name"
            )

    # CORE CONTRACT 
    @abstractmethod
    def search(self, intent: SearchIntent) -> List[RawJob]:
        """
        Thực hiện search job dựa trên SearchIntent.
        - Không filter sâu
        - Không scoring
        - Không matching
        - Chỉ thu thập + chuẩn hóa RawJob
        """
        raise NotImplementedError

    # OPTIONAL HOOKS 
    def build_source_meta(
        self,
        url: str | None = None,
        raw_id: str | None = None
    ) -> SourceMeta:
        """
        Helper chuẩn hóa metadata nguồn.
        Adapter con có thể override nếu cần.
        """
        return SourceMeta(
            platform=self.platform_name,
            url=url,
            raw_id=raw_id,
            collected_at=datetime.utcnow()
        )

