import re
from typing import Optional, Dict, List


# Chuẩn hóa vị trí từ JD
def normalize_location(text: Optional[str]) -> Optional[List[Dict]]:
    if not text:
        return None

    raw = text.strip()
    # Loại bỏ các thông báo kiểu "(đã được cập nhật theo ...)" Cho TopCV
    raw = re.sub(r"\(.*?cập nhật.*?\)", "", raw, flags=re.IGNORECASE)
    # Loại bỏ dấu "-"
    raw = raw.replace("-", " ")

    raw_lc = raw.lower()
    
    # print("Raw location" + raw)

    # Nếu Job yêu cầu remote thì return lun
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

    # Cắt nếu có nhiều vì trí
    parts = split_by_city(raw)
    for part in parts:
        loc = normalize_single_location(part.strip())
        if loc:
            locations.append(loc)

    return locations or None

# Chuẩn hóa từng vị trí và trích thông tin địa điểm làm việc
def normalize_single_location(raw: str) -> Optional[List[Dict]]:
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
    
    # Remove city prefix nếu có
    if ":" in raw:
        raw_for_address = raw.split(":", 1)[1].strip()
    else:
        raw_for_address = raw

    # trích thành phố
    city = extract_city(raw_lc)
    if city:
        location["city"] = city
        location["country"] = "Vietnam"
        location["confidence"] += 0.5
        location["granularity"] = "city"

    segments = split_address_segments(raw_for_address)

    for seg in segments:
        if not location["street"]:
            # Trích đường
            street = extract_street(seg)
            if street:
                location["street"] = street
                location["confidence"] += 0.15
                location["granularity"] = "address"
                continue

        if not location["ward"]:
            # Trích phường xã
            ward = extract_ward(seg)
            if ward:
                location["ward"] = ward
                location["confidence"] += 0.15
                location["granularity"] = "address"
                continue

        if not location["district"]:
            # Trích huyện quân
            district = extract_district(seg)
            if district:
                location["district"] = district
                location["confidence"] += 0.2
                location["granularity"] = "district"

    # Nếu confidence quá thấp thì bỏ
    if location["confidence"] < 0.3:
        location["type"] = "unknown"
        location["granularity"] = "unknown"
        location["confidence"] = round(location["confidence"], 2)
        return location

    location["confidence"] = round(min(location["confidence"], 1.0), 2)
    return location

# Kiếm tra xem có phải làm từ xa
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
def extract_street(text: str, city: Optional[str] = None) -> Optional[str]:
    text_lc = text.lower()

    # Không có thành phố → không trích street
    if not city:
        return None

    # bỏ qua nếu chứa keyword không hộp lệ với đường
    if any(k in text_lc for k in ADMIN_KEYWORDS):
        return None

    # Ưu tiên tên đường có số
    street_found = STREET_WITH_NUMBER_PATTERN.search(text)
    if street_found:
        return clean_street(street_found.group())

    # chỉ tên đường
    street_found = STREET_NAME_PATTERN.search(text)
    if street_found:
        street = clean_street(street_found.group())

        # tên quá chung → bỏ
        if len(street.split()) < 2:
            return None

        return street

    return None

# Hàm clean các giá trị ko cần thiết như khoản cách xuống dồng hoặc các ký tự thừa ở đầu và cuối
def clean_street(street: str) -> str:
    if not street:
        return street

    s = street.strip()

    # Gộp nhiều khoảng trắng
    s = re.sub(r"\s{2,}", " ", s)

    # Bỏ dấu phân cách thừa ở đầu/cuối
    s = s.strip(" ,.-")

    # Chuẩn hóa prefix (nhẹ, không đoán)
    s = re.sub(
        r"^(đường|street|st\.?)\s+",
        "",
        s,
        flags=re.IGNORECASE
    )

    return s

# Tách các dịa chỉ bằng thành phố
def split_by_city(raw: str) -> List[str]:
    chunks = []
    last = 0

    for m in re.finditer(r"(Hồ\s*Chí\s*Minh|Hà\s*Nội|Đà\s*Nẵng)", raw, re.IGNORECASE):
        if last != m.start():
            chunks.append(raw[last:m.start()].strip())
        last = m.start()

    chunks.append(raw[last:].strip())
    return [c for c in chunks if c]

# Tách dịa chỉ thành nhiều dồng để dê trích xuất quận, phường , đường
def split_address_segments(text: str) -> list[str]:
    ""
    # Ví dụ "12 Nguyễn Huệ, Phường Bến Nghé, Quận 1, Hồ Chí Minh"
    # Sẽ tách thành
    #   "12 Nguyễn Huệ",
    #   "Phường Bến Nghé",
    #   "Quận 1",
    #   "Hồ Chí Minh"
    ""
    return [seg.strip() for seg in text.split(",") if seg.strip()]


# ---------- PATTERNS ----------
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
    r"(phường|p\.?|ward)\s+([A-Za-zÀ-ỹ0-9\s]{1,30})$",
    re.IGNORECASE
)

# Từ khóa ko cần thiết
INVALID_WARD_KEYWORDS = [
    "hành chính",
    "danh mục",
    "cập nhật",
    "theo",
]

# ----- Các pattern cho việc trích đường -----
# Tên đường kèm theo số
STREET_WITH_NUMBER_PATTERN = re.compile(
    r"""
    (?:tầng\s*\d+,\s*)?
    (?:số\s*)?
    \d+[A-Za-z]?
    [,\s]+
    [A-Za-zÀ-ỹ][A-Za-zÀ-ỹ0-9\s.-]{3,}
    """,
    re.IGNORECASE | re.VERBOSE
)

# Tên đường không có số
STREET_NAME_PATTERN = re.compile(
    r"""
    (?:đường\s+)?                 
    [A-Za-zÀ-ỹ][A-Za-zÀ-ỹ\s.-]{4,}
    """,
    re.IGNORECASE | re.VERBOSE
)

# Các key phải tránh khi trích tên đường
ADMIN_KEYWORDS = [
    "phường", "ward",
    "quận", "district",
    "huyện",
    "thành phố", "tp", "city",
    "việt nam", "vietnam"
]
