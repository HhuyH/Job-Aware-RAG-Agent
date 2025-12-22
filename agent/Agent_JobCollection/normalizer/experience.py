import re
from typing import Optional, Dict, List


# =========================
# PUBLIC API
# =========================

def extract_experience(text: str) -> Optional[Dict]:
    """
    Extract experience requirements from JD text.

    Return:
    {
        min_years: float | None,
        max_years: float | None,
        levels: List[str],
        signals: List[Dict],
        raw_texts: List[str]
    }
    """
    if not text:
        return None

    text_lc = text.lower()

    signals: List[Dict] = []
    raw_texts: List[str] = []
    mins: List[float] = []
    maxs: List[float] = []
    levels: set[str] = set()

    # 1. No-experience signals (KHÔNG return sớm)
    for p in NO_EXP_PATTERNS:
        if re.search(p, text_lc):
            signals.append({
                "type": "no_experience",
                "raw": p
            })
            levels.update({"intern", "junior"})
            mins.append(0.0)
            maxs.append(0.0)

    # 2. Range with plus: 1–3+ years
    for m in re.finditer(RANGE_PLUS_PATTERN, text_lc):
        min_y = float(m.group("min"))
        mins.append(min_y)
        signals.append({
            "type": "range_plus",
            "raw": m.group(0)
        })
        raw_texts.append(m.group(0))
        levels.update(infer_levels(min_y, None))

    # 3. Range: 1–3 years
    for m in re.finditer(RANGE_PATTERN, text_lc):
        min_y = float(m.group("min"))
        max_y = float(m.group("max"))
        mins.append(min_y)
        maxs.append(max_y)
        signals.append({
            "type": "range",
            "raw": m.group(0)
        })
        raw_texts.append(m.group(0))
        levels.update(infer_levels(min_y, max_y))

    # 4. Minimum: at least X years
    for m in re.finditer(MIN_PATTERN, text_lc):
        min_y = float(m.group("min"))
        mins.append(min_y)
        signals.append({
            "type": "minimum",
            "raw": m.group(0)
        })
        raw_texts.append(m.group(0))
        levels.update(infer_levels(min_y, None))

    # 5. X+ years
    for m in re.finditer(PLUS_PATTERN, text_lc):
        min_y = float(m.group("min"))
        mins.append(min_y)
        signals.append({
            "type": "plus",
            "raw": m.group(0)
        })
        raw_texts.append(m.group(0))
        levels.update(infer_levels(min_y, None))

    if not signals:
        return None

    return {
        "min_years": min(mins) if mins else None,
        "max_years": max(maxs) if maxs else None,
        "levels": sorted(levels),
        "signals": signals,
        "raw_texts": raw_texts
    }


# =========================
# LEVEL INFERENCE (IN FILE)
# =========================

def infer_levels(min_years: Optional[float], max_years: Optional[float]) -> List[str]:
    """
    Infer seniority levels from experience years.
    """
    levels = set()

    if min_years is None:
        return []

    if min_years == 0:
        levels.update(["intern", "junior"])

    if min_years <= 1:
        levels.add("junior")

    if max_years is None:
        if min_years >= 3:
            levels.update(["mid", "senior"])
    else:
        if max_years >= 2:
            levels.add("mid")
        if max_years >= 5:
            levels.add("senior")

    return list(levels)


# =========================
# PATTERNS
# =========================

NO_EXP_PATTERNS = [
    r"no experience",
    r"without experience",
    r"fresher",
    r"fresh graduate",
    r"sinh viên",
    r"thực tập",
    r"intern",
    r"mới ra trường",
]

RANGE_PATTERN = re.compile(
    r"(?P<min>\d+(?:\.\d+)?)\s*(?:-|–|to)\s*(?P<max>\d+(?:\.\d+)?)\s*(năm|years?)"
)

RANGE_PLUS_PATTERN = re.compile(
    r"(?P<min>\d+(?:\.\d+)?)\s*(?:-|–|to)\s*(?P<max>\d+(?:\.\d+)?)\s*\+\s*(năm|years?)"
)

MIN_PATTERN = re.compile(
    r"(tối thiểu|ít nhất|minimum|at least)\s*(?P<min>\d+(?:\.\d+)?)\s*(năm|years?)"
)

PLUS_PATTERN = re.compile(
    r"(?P<min>\d+(?:\.\d+)?)\s*\+\s*(năm|years?)"
)
