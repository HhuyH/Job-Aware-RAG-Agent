from agent.Agent_Resume.perception import extract_resume_text
from agent.Agent_Resume.structuring_v2 import structure_cv
from agent.Agent_Resume.resolve_unresolved_llm import resolve_unresolved
from agent.Agent_Resume.extraction import extract_from_sections
from common.section_logger import log_sections
from common.logger import get_logger

logger = get_logger("agent.resume.structuring")

if __name__ == "__main__":
    
    # Chuyển file cv pdf thành text thô
    raw_text = extract_resume_text()
    
    # logger.info("Extracted Text:\n%s", raw_text)

    # Chia cấu trúc CV từ text thô
    structured = structure_cv(raw_text)
    
    # Giải quyết các dòng 'unresolved' bằng LLM

    structured = resolve_unresolved(
        structured=structured,
        unresolved_text=structured.get("unresolved", ""),
    )
    
    structured.pop("unresolved", None)

    # In ra section đã chia
    # log_sections(structured, only=["UNRESOLVED"])
    
    # In ra tất cả section đã làm sạch
    log_sections(structured)
    
    # Log json file các section đã chia
    # extract_from_sections(structured)
    
