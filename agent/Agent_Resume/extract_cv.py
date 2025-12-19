from agent.Agent_Resume.perception import extract_resume_text
from agent.Agent_Resume.structuring_v2 import structure_cv
from agent.Agent_Resume.resolve_unresolved_llm import resolve_unresolved
from agent.Agent_Resume.extraction import extract_from_sections
from common.json_logger import dump_json
from pathlib import Path
import json
from common.section_logger import log_sections
from common.logger import get_logger

logger = get_logger("agent.resume.structuring")

if __name__ == "__main__":
    
    # Chuyển file cv pdf thành text thô
    # raw_text = extract_resume_text("LeNguyenHoanHuy_AI_Engineer_Fresher_CV.pdf")
    
    # logger.info("Extracted Text:\n%s", raw_text)

    # Chia cấu trúc CV từ text thô
    # structured = structure_cv(raw_text)
    
    # Giải quyết các dòng 'unresolved' bằng LLM
    # structured = resolve_unresolved(
    #     structured=structured,
    #     unresolved_text=structured.get("unresolved", ""),
    # )
    
    # structured.pop("unresolved", None)

    # Lưu cấu trúc đã chia vào file cache để tranh chay lại llm
    # CACHE_FILE = Path("cache/structured_resolved.json")
    # CACHE_FILE.parent.mkdir(exist_ok=True)
    # CACHE_FILE.write_text(
    #     json.dumps(structured, ensure_ascii=False, indent=2),
    #     encoding="utf-8"
    # )

    # Đọc lại file cache đã lưu
    CACHE_FILE = Path("cache/structured_resolved.json")
    if CACHE_FILE.exists():
        structured = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    else:
        raise FileNotFoundError(f"{CACHE_FILE} not found.")
        
    # In ra section đã chia
    # log_sections(structured, only=["UNRESOLVED"])
    
    # In ra tất cả section đã làm sạch
    # log_sections(structured)

    # Trích xuất thông tin từ các section đã chia và lưu vào excel
    extract_from_sections(structured)
    
    
