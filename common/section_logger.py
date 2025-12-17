from typing import Dict, Iterable
from common.logger import get_logger

logger = get_logger("agent.section_logger")


def log_sections(
    sections: Dict[str, str],
    only: Iterable[str] | None = None,
    preview: int = 5000
):
    """
    Log selected sections only.
    - only: list section names to log, None = all
    - preview: number of characters to show
    """
    targets = {sec.lower(): sec for sec in sections.keys()}
    for sec_name in (only or sections.keys()):
        key = sec_name.lower()
        if key not in targets:
            logger.warning("Section [%s] not found", sec_name)
            continue
        content = sections[targets[key]]
        logger.info(
            "\n--- %s ---\n%s%s\n",
            sec_name,
            content[:preview],
            "..." if len(content) > preview else ""
        )

