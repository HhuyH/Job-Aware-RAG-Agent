import re
from typing import Optional, Dict, List


# Chuẩn hóa vị trí từ raw JD
def normalize_location(text: Optional[str]) -> Optional[List[Dict]]:
    if not text:
        return None

    raw = text.strip()
    # Loại bỏ các thông báo kiểu "(đã được cập nhật theo ...)"
    raw = re.sub(r"\(.*?cập nhật.*?\)", "", raw, flags=re.IGNORECASE)
    # Loại bỏ dấu "-"
    raw = raw.replace("-", " ")

    raw_lc = raw.lower()
    
    # print("Raw location" + raw)

    # Remote
    if is_remote(raw_lc):
        return [{
            "raw": raw,
            "type": "remote",
            "country": None,
            "city": None,
            "district": None,
            "ward": None,
            "street": None,
            "granularity": "remote",
            "confidence": 1.0
        }]

    locations: List[Dict] = []

    # Cát nhiều vì trí
    parts = re.split(r"[\/|]+", raw)
    for part in parts:
        loc = _normalize_single_location(part.strip())
        if loc:
            locations.append(loc)

    return locations or None


# 1 vị trí
def _normalize_single_location(raw: str) -> Optional[Dict]:
    raw_lc = raw.lower()
    
    location = {
        "raw": raw,
        "type": "onsite",
        "country": None,
        "city": None,
        "district": None,
        "ward": None,
        "street": None,
        "granularity": "unknown",
        "confidence": 0.0
    }

    # trích thành phố
    city = extract_city(raw_lc)
    if city:
        location["city"] = city
        location["country"] = "Vietnam"
        location["confidence"] += 0.5
        location["granularity"] = "city"

    # Remove city prefix nếu có
    if ":" in raw:
        raw_for_address = raw.split(":", 1)[1].strip()
    else:
        raw_for_address = raw

    # Trích quận huyện
    district = extract_district(raw_for_address)
    if district:
        location["district"] = district
        location["confidence"] += 0.2
        location["granularity"] = "district"

    # Trích phường xã
    ward = extract_ward(raw_for_address)
    if ward:
        location["ward"] = ward
        location["confidence"] += 0.15
        location["granularity"] = "address"

    # Trích đường
    street = extract_street(raw_for_address)
    if street:
        location["street"] = street
        location["confidence"] += 0.15
        location["granularity"] = "address"

    # Nếu confidence quá thấp thì bỏ
    if location["confidence"] < 0.3:
        return None

    location["confidence"] = round(min(location["confidence"], 1.0), 2)
    return location

# Kiếm tra xem có phải làm từ xa hay không
def is_remote(text: str) -> bool:
    return any(k in text for k in [
        "remote",
        "work from home",
        "wfh",
        "anywhere"
    ])

# Trích thành phố
def extract_city(text: str) -> Optional[str]:
    for city, pattern in CITY_PATTERNS.items():
        if re.search(pattern, text):
            return city
    return None

# Trích Quân huyện
def extract_district(text: str) -> Optional[str]:
    m = DISTRICT_PATTERN.search(text)
    if m:
        return f"District {m.group(2)}"
    return None

# Trích Phường xã
def extract_ward(text: str) -> Optional[str]:
    m = WARD_PATTERN.search(text)
    if not m:
        return None

    ward = m.group(2).strip()

    ward_lc = ward.lower()
    if any(k in ward_lc for k in INVALID_WARD_KEYWORDS):
        return None

    return ward

# Trích đường
def extract_street(text: str) -> Optional[str]:
    m = STREET_PATTERN.search(text)
    if m:
        return clean_street(m.group())
    return None

# Hàm làm sạch tên đường
def clean_street(street: str) -> str:
    # Gộp nhiều khoảng trắng liên tiếp thành một khoảng trắng
    street = re.sub(r"\s{2,}", " ", street)
    # Loại bỏ các ký tự phân cách dư ở đầu/cuối
    return street.strip(",.- ")

# Clean 1 số thứ không cần thiết
def clean_location_raw(raw: str) -> str:
    # Loại bỏ các thông báo kiểu "(đã được cập nhật theo ...) của TopCV"
    raw = re.sub(r"\(.*?cập nhật.*?\)", "", raw, flags=re.IGNORECASE)
    # Loại bỏ dấu "-"
    raw = raw.replace("-", " ")
    return raw.strip()

# ------- PATTERNS -------
# Thành phố
CITY_PATTERNS = {
    "Ho Chi Minh": r"hồ\s*chí\s*minh|tp\.?\s*hcm|hcm\b|ho\s*chi\s*minh",
    "Ha Noi": r"hà\s*nội|ha\s*noi",
    "Da Nang": r"đà\s*nẵng|da\s*nang",
    "Binh Duong": r"bình\s*dương|binh\s*duong",
    "Dong Nai": r"đồng\s*nai|dong\s*nai",
}

# Quận huyện
DISTRICT_PATTERN = re.compile(
    r"(quận|q\.?|huyện)\s*(?P<district>[A-Za-zÀ-ỹ0-9\s]+)",
    re.IGNORECASE
)

# Phường xã
WARD_PATTERN = re.compile(
    r"(phường|p\.?|ward)\s*([A-Za-zÀ-ỹ0-9\s,.-]{1,50})", re.IGNORECASE
)

# Từ khóa ko cần thiết
INVALID_WARD_KEYWORDS = [
    "hành chính",
    "danh mục",
    "cập nhật",
    "theo",
]

# Đường
STREET_PATTERN = re.compile(
    r"((?:tầng\s*\d+,\s*)?(?:số\s*\d+,\s*)?(?:đường|street)\s+[A-Za-zÀ-ỹ0-9\s,.-]+)", re.IGNORECASE
)
