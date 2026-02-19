import json
from datetime import datetime
import math

_frame_count = 0
_event_log_initialized = False
_start_time = datetime.now()


def log_event(event_type, **details):
    global _event_log_initialized

    now = datetime.now()

    event = {
        "timestamp": now.strftime("%H:%M:%S.%f")[:-3],
        "elapsed_s": math.floor((now - _start_time).total_seconds()),
        "frame": _frame_count,
        "type": event_type,
        **details,
    }

    mode = "w" if not _event_log_initialized else "a"
    with open("game_events.jsonl", mode) as f:
        f.write(json.dumps(event) + "\n")

    _event_log_initialized = True