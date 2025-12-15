from agent.Agent_Resume.perception import extract_resume_text
from agent.Agent_Resume.structuring import structure_cv

if __name__ == "__main__":
    structure_cv(extract_resume_text())
