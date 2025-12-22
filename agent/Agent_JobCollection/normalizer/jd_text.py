import re
import unicodedata
from bs4 import BeautifulSoup
from typing import Optional

# Chuẩn hóa JD: HTML → text sạch
def clean_jd_text(
    raw_html_or_text: Optional[str]
) -> str:

    if not raw_html_or_text:
        return ""

    text = raw_html_or_text

    # 1. HTML → text
    if "<" in text and ">" in text:
        text = _html_to_text(text)

    # 2. Normalize unicode
    text = _normalize_unicode(text)

    # 3. Normalize bullets
    text = _normalize_bullets(text)

    # 4. Remove noise lines
    text = _remove_noise_lines(text)

    # 5. Normalize whitespace
    text = _normalize_whitespace(text)

    return text.strip()

def _html_to_text(html: str) -> str:
    """
    Chuyển HTML thô sang plain text để phục vụ cho các bước xử lý tiếp theo
    (regex, NLP, trích xuất kỹ năng, kinh nghiệm, v.v.)

    Mục đích chính:
    - Loại bỏ toàn bộ markup HTML
    - Loại bỏ các tag gây nhiễu (script, style, noscript)
    - Giữ lại nội dung text thuần, có xuống dòng để dễ phân tích

    Hàm này KHÔNG nhằm tạo văn bản đẹp để hiển thị,
    mà nhằm tạo dữ liệu đầu vào ổn định cho pipeline normalize.
    """

    # Parse HTML bằng BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Loại bỏ các tag không chứa nội dung văn bản hữu ích
    # (JS, CSS, nội dung fallback)
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Lấy toàn bộ text trong HTML
    # separator="\n" giúp:
    # - Giữ ranh giới giữa các block (div, p, li, ...)
    # - Tránh dính chữ gây khó regex / NLP
    text = soup.get_text(separator="\n")

    return text

# Chuẩn hóa unicode
def _normalize_unicode(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    return text

# Chuẩn hóa bullet: - •, -, *, → "- "
def _normalize_bullets(text: str) -> str:
    text = re.sub(r"[•●▪◦]+", "-", text)
    text = re.sub(r"\n\s*[-*]\s*", "\n- ", text)
    return text

# Remove các dòng UI / CTA / legal
def _remove_noise_lines(text: str) -> str:
    noise_patterns = [
        r"ứng tuyển ngay",
        r"apply now",
        r"click here",
        r"quyền lợi",
        r"phúc lợi",
        r"chế độ đãi ngộ",
        r"liên hệ",
        r"hotline",
        r"facebook",
        r"zalo",
        r"website",
        r"www\.",
        r"http[s]?:\/\/",
    ]

    lines = []
    for line in text.splitlines():
        line_clean = line.strip()
        if not line_clean:
            continue

        is_noise = False
        for p in noise_patterns:
            if re.search(p, line_clean, flags=re.IGNORECASE):
                is_noise = True
                break

        if not is_noise:
            lines.append(line_clean)

    return "\n".join(lines)

# Chuẩn hóa lỗi bỏ các khoản cách và xuồng dòng du thừa
def _normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text
