# Trích xuất văn bản từ PDF: Dùng pdfminer để đọc toàn bộ nội dung text từ file PDF.
# Làm sạch văn bản: Loại bỏ khoảng trắng dư thừa, chuẩn hóa các tab, và gom các dòng trống liên tiếp để text dễ xử lý hơn sau này.

# Các hàm chính:
# - extract_text_from_pdf(pdf_path): Nhận đường dẫn PDF, trả về toàn bộ text thô.
# - clean_text(text): Chuẩn hóa text, loại bỏ khoảng trắng và các dòng trống dư thừa.
# - extract_resume_text(pdf_file): Tích hợp trích xuất + làm sạch, nhận tên file PDF trong thư mục resumes, trả về text đã sạch. Đồng thời ghi log các bước quan trọng (nếu file không tồn tại, ghi lỗi).

from pdfminer.high_level import extract_text
import re
from pathlib import Path
from common.logger import get_logger

logger = get_logger("agent.resume.perception")

BASE_DIR = Path(__file__).resolve().parents[2]
RESUME_DIR = BASE_DIR / "resumes"

def extract_text_from_pdf(pdf_path: Path) -> str:
    return extract_text(str(pdf_path))

def clean_text(text: str) -> str:
    if not text:
        return ""

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def extract_resume_text(pdf_file: str = None) -> str:
    pdf_path = RESUME_DIR / pdf_file

    # logger.info("BASE_DIR=%s", BASE_DIR)
    # logger.info("RESUME_DIR=%s", RESUME_DIR)

    if not pdf_path.exists():
        logger.error("PDF not found: %s", pdf_path)
    else:
        raw = extract_text_from_pdf(pdf_path)
        cleaned = clean_text(raw)
        logger.debug("Extracted %d characters", len(cleaned))
    
    return cleaned
