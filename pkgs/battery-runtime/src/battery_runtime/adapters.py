import json
import sys
import time
from typing import Any


class StdInSource:
    """Reads JSON lines from stdin (non-blocking-ish if piped)."""

    def read(self) -> dict[str, Any] | None:
        try:
            line = sys.stdin.readline()
            if not line:
                return None
            return json.loads(line)
        except Exception:
            return None


class StdOutSink:
    def write(self, record: dict[str, Any]) -> None:
        print(json.dumps(record, separators=(",", ":")))
        sys.stdout.flush()


class SyntheticSource:
    """Simple simulator: emits {a, z} for toy KF."""

    def __init__(self):
        self.t0 = time.monotonic()
        self.pos = 0.0
        self.vel = 1.0

    def read(self) -> dict[str, Any]:
        t = time.monotonic() - self.t0
        a = 0.0
        z = self.pos  # "measurement"
        # advance truth for next step
        self.pos += self.vel * 0.02
        return {"t_source": t, "a": a, "z": z}
