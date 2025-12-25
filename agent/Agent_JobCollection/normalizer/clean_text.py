#File này có nhiệm vũ chuẩn hóa JD thành text

import re
import unicodedata
from bs4 import BeautifulSoup
from typing import Optional

# Chuẩn hóa JD
def clean_jd_text(
    raw_html_or_text: Optional[str]
) -> str:

    if not raw_html_or_text:
        return ""

    text = raw_html_or_text

    # HTML → text
    if "<" in text and ">" in text:
        text = html_to_text(text)

    # Chuẩn hóa unicode
    text = normalize_unicode(text)

    # Chuẩn hóa các bullet đầu dồng
    text = normalize_bullets(text)

    # Xóa cách thông tin không cần thiết
    text = remove_noise_lines(text)

    # Chuẩn hóa các khoản cách và xuồng dòng du thừa để đồng bộ
    text = normalize_whitespace(text)

    return text.strip()

# Chuyển html về text
def html_to_text(html: str) -> str:
    # Lấy nội dung HTML ban đầu 
    soup = BeautifulSoup(html, "html.parser")

    # Loại bỏ các lệnh ko cần thiết để phục vụ cho LLM có 1 số HTML kềm lệnh như window.dataLayer.push({...});
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # .get_text loại bỏ các tag <h3> <ul>... và thay thế chúng bằng "\n"
    # <h3>Responsibilities</h3>
    # <ul>
    #     <li>Build AI models</li>
    #     <li>Use Python</li>
    # </ul>
    text = soup.get_text(separator="\n")

    return text

# Chuẩn hóa unicode
def normalize_unicode(text: str) -> str:
    # NFKC Normalization Form Compatibility Composition chuyển các kỹ tự khác nhau như khác vể front khác full-width thành 1 kieu ví dụ
    # "AI Engineer"
    # "AＩ Engineer"
    # Nhìn có vễ giống những máy sẽ thấy khác vì vậy nên cần NFKC này để chuyển về 1 kiểu
    text = unicodedata.normalize("NFKC", text)
    return text

# Thay đổi các dấu thành 1 dấu hoặc khoản cách xuống dồng khác nhau thành 1 dấu đồng nhất để dễ xữ lý
def normalize_bullets(text: str) -> str:
    text = re.sub(r"[•●▪◦]+", "-", text)
    text = re.sub(r"\n\s*[-*]\s*", "\n- ", text)
    return text

# Remove các thông tin không cần thiết 
def remove_noise_lines(text: str) -> str:
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

# Chuẩn hóa các khoản cách và xuồng dòng du thừa để đồng bộ
def normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text
