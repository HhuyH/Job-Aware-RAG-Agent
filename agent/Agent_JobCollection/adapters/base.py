# Abstract class bắt buộc raw JD từ tất cả nền tảng điểu phải thống nhất 1 cấu trúc
from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from ..schema import SearchIntent, RawJob, SourceMeta

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

    # Cấu trúc source meta(có thể overrdie)
    def build_source_meta(
        self,
        url: str | None = None,
        raw_id: str | None = None
    ) -> SourceMeta:
        """
        - platform: tên nền tảng
        - url: link gốc job
        - raw_id: id của job trên nền tảng
        - collected_at: thời gian thu thập
        """
        return SourceMeta(
            platform=self.platform_name,
            url=url,
            raw_id=raw_id,
            collected_at=datetime.utcnow()
        )

