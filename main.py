from agent.Agent_Resume.perception import extract_resume_text
from agent.Agent_Resume.structuring import structure_cv
from agent.Agent_Resume.extraction import extract_from_sections
from common.logger import get_logger

logger = get_logger("agent.resume.structuring")

if __name__ == "__main__":
    
    # cleaned = extract_resume_text()
    # logger.info("Extracted Text:\n%s", cleaned)
    
    structure_cv(extract_resume_text())
    
    # extract_from_sections(structure_cv(extract_resume_text()))
    
