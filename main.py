from agent.Agent_Resume.perception import extract_resume_text
from agent.Agent_Resume.structuring_v2 import structure_cv
from agent.Agent_Resume.extraction import extract_from_sections
from common.logger import get_logger

logger = get_logger("agent.resume.structuring")

if __name__ == "__main__":
    
    # Chuyển file cv pdf thành text thô
    raw_text = extract_resume_text()
    
    # logger.info("Extracted Text:\n%s", raw_text)

    # Chia cấu trúc CV từ text thô
    structured = structure_cv(raw_text)

    # Log json file các section đã chia
    # extract_from_sections(structured)
    
