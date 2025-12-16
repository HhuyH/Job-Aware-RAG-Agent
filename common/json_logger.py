import json
from pathlib import Path
from datetime import datetime
from typing import Any


def dump_json(
    data: Any,
    base_dir: Path,
    prefix: str = "output"
) -> Path:
    base_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = base_dir / f"{prefix}_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return file_path
