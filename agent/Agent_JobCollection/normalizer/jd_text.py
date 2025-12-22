import re
import unicodedata
from bs4 import BeautifulSoup
from typing import Optional


# PUBLIC API
def clean_jd_text(
    raw_html_or_text: Optional[str]
) -> str:
    """
    Chuẩn hóa JD:
    HTML → text sạch
    """
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



# INTERNAL HELPERS
def _html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Remove noise tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    return text


def _normalize_unicode(text: str) -> str:
    """
    Chuẩn hóa unicode:
    - remove weird chars
    - normalize accents
    """
    text = unicodedata.normalize("NFKC", text)
    return text


def _normalize_bullets(text: str) -> str:
    """
    Chuẩn hóa bullet:
    - •, -, *, → "- "
    """
    text = re.sub(r"[•●▪◦]+", "-", text)
    text = re.sub(r"\n\s*[-*]\s*", "\n- ", text)
    return text


def _remove_noise_lines(text: str) -> str:
    """
    Remove các dòng UI / CTA / legal
    """
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


def _normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text
