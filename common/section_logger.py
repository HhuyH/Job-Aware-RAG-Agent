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
    targets = only or sections.keys()

    for sec in targets:
        if sec not in sections:
            logger.warning("Section [%s] not found", sec)
            continue

        content = sections[sec]
        logger.info(
            "\n--- %s ---\n%s%s\n",
            sec,
            content[:preview],
            "..." if len(content) > preview else ""
        )
