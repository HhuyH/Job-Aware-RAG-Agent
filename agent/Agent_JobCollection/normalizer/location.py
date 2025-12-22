import re
from typing import Optional, Dict, List


# =========================
# PUBLIC API
# =========================

def normalize_location(text: Optional[str]) -> Optional[List[Dict]]:
    """
    Normalize job location(s) from raw text.
    Return list of location dicts.
    """
    if not text:
        return None

    raw = text.strip()
    # Loại bỏ các thông báo kiểu "(đã được cập nhật theo ...)"
    raw = re.sub(r"\(.*?cập nhật.*?\)", "", raw, flags=re.IGNORECASE)
    # Loại bỏ dấu "-"
    raw = raw.replace("-", " ")

    raw_lc = raw.lower()
    
    print("Raw location" + raw)

    # Remote
    if _is_remote(raw_lc):
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

    # Split multi-locations
    parts = re.split(r"[\/|]+", raw)
    for part in parts:
        loc = _normalize_single_location(part.strip())
        if loc:
            locations.append(loc)

    return locations or None


# =========================
# SINGLE LOCATION
# =========================

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

    # 1️⃣ Extract city
    city = _extract_city(raw_lc)
    if city:
        location["city"] = city
        location["country"] = "Vietnam"
        location["confidence"] += 0.5
        location["granularity"] = "city"

    # 2️⃣ Remove city prefix nếu có
    if ":" in raw:
        raw_for_address = raw.split(":", 1)[1].strip()
    else:
        raw_for_address = raw

    # 3️⃣ Extract district
    district = _extract_district(raw_for_address)
    if district:
        location["district"] = district
        location["confidence"] += 0.2
        location["granularity"] = "district"

    # 4️⃣ Extract ward
    ward = _extract_ward(raw_for_address)
    if ward:
        location["ward"] = ward
        location["confidence"] += 0.15
        location["granularity"] = "address"

    # 5️⃣ Extract street
    street = _extract_street(raw_for_address)
    if street:
        location["street"] = street
        location["confidence"] += 0.15
        location["granularity"] = "address"

    # Nếu confidence quá thấp thì bỏ
    if location["confidence"] < 0.3:
        return None

    location["confidence"] = round(min(location["confidence"], 1.0), 2)
    return location


# =========================
# HELPERS
# =========================

def clean_location_raw(raw: str) -> str:
    # Loại bỏ các thông báo kiểu "(đã được cập nhật theo ...)"
    raw = re.sub(r"\(.*?cập nhật.*?\)", "", raw, flags=re.IGNORECASE)
    # Loại bỏ dấu "-"
    raw = raw.replace("-", " ")
    return raw.strip()

def _is_remote(text: str) -> bool:
    return any(k in text for k in [
        "remote",
        "work from home",
        "wfh",
        "anywhere"
    ])


# CITY
CITY_PATTERNS = {
    "Ho Chi Minh": r"hồ\s*chí\s*minh|tp\.?\s*hcm|hcm\b|ho\s*chi\s*minh",
    "Ha Noi": r"hà\s*nội|ha\s*noi",
    "Da Nang": r"đà\s*nẵng|da\s*nang",
    "Binh Duong": r"bình\s*dương|binh\s*duong",
    "Dong Nai": r"đồng\s*nai|dong\s*nai",
}

def _extract_city(text: str) -> Optional[str]:
    for city, pattern in CITY_PATTERNS.items():
        if re.search(pattern, text):
            return city
    return None


# DISTRICT
DISTRICT_PATTERN = re.compile(
    r"(quận|q\.?|huyện)\s*(?P<district>[A-Za-zÀ-ỹ0-9\s]+)",
    re.IGNORECASE
)

def _extract_district(text: str) -> Optional[str]:
    m = DISTRICT_PATTERN.search(text)
    if m:
        return f"District {m.group(2)}"
    return None


# WARD
WARD_PATTERN = re.compile(
    r"(phường|p\.?|ward)\s*([A-Za-zÀ-ỹ0-9\s,.-]{1,50})", re.IGNORECASE
)

INVALID_WARD_KEYWORDS = [
    "hành chính",
    "danh mục",
    "cập nhật",
    "theo",
]

def _extract_ward(text: str) -> Optional[str]:
    m = WARD_PATTERN.search(text)
    if not m:
        return None

    ward = m.group(2).strip()

    ward_lc = ward.lower()
    if any(k in ward_lc for k in INVALID_WARD_KEYWORDS):
        return None

    return ward


# STREET
STREET_PATTERN = re.compile(
    r"((?:tầng\s*\d+,\s*)?(?:số\s*\d+,\s*)?(?:đường|street)\s+[A-Za-zÀ-ỹ0-9\s,.-]+)", re.IGNORECASE
)

def _extract_street(text: str) -> Optional[str]:
    m = STREET_PATTERN.search(text)
    if m:
        return _clean_street(m.group())
    return None


def _clean_street(street: str) -> str:
    street = re.sub(r"\s{2,}", " ", street)
    return street.strip(",.- ")
