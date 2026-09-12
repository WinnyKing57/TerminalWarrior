import json
from pathlib import Path

SAVE_PATH = Path.home() / ".terminal_warrior_progress.json"


def load_progress():
    if SAVE_PATH.exists():
        try:
            data = json.loads(SAVE_PATH.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "linux" in data and "windows" in data:
                return data
        except (json.JSONDecodeError, OSError):
            pass
    return {"linux": {}, "windows": {}}


def save_progress(data):
    try:
        SAVE_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    except OSError:
        pass


def is_done(data, os_name, number):
    return bool(data.get(os_name, {}).get(str(number), {}).get("done"))


def mark_done(data, os_name, number, elapsed=None):
    key = str(number)
    entry = dict(data.get(os_name, {}).get(key, {}))
    if not entry.get("done"):
        entry = {"done": True}
        entry["score"] = points_for(os_name, key)
        if elapsed is not None:
            entry["time"] = round(elapsed, 1)
    elif elapsed is not None:
        best = entry.get("time")
        if best is None or elapsed < best:
            entry["time"] = round(elapsed, 1)
    data.setdefault(os_name, {})[key] = entry


def points_for(os_name, number):
    number = int(number)
    if os_name == "linux" and number == 20:
        return 25
    if os_name == "windows" and number == 25:
        return 25
    return 10


def get_score(data):
    total = 0
    for os_name in ("linux", "windows"):
        for key, value in data.get(os_name, {}).items():
            if value.get("done"):
                total += points_for(os_name, key)
    return total


def count_done(data, os_name):
    return sum(1 for v in data.get(os_name, {}).values() if v.get("done"))


def format_time(seconds):
    if seconds is None:
        return ""
    seconds = int(seconds)
    m, s = divmod(seconds, 60)
    if m:
        return f"{m}m {s:02d}s"
    return f"{s}s"