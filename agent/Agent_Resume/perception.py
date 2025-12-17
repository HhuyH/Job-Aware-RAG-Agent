# trích xuất và làm sạch text từ file PDF resume

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

def extract_resume_text():
    pdf_file = "LeNguyenHoanHuy_AI_Engineer_Fresher_CV.pdf"
    # pdf_file = "Manhattan.pdf"
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
