import time
from typing import Callable


class FixedRate:
    def __init__(self, hz: int = 50, max_jitter_ms: float = 5.0):
        self.period = 1.0 / hz
        self.max_jitter_ms = max_jitter_ms

    def run(self, fn: Callable[[float, float], None], duration_s: float | None = None):
        start = time.monotonic()
        next_t = start + self.period
        last = start
        while True:
            now = time.monotonic()
            dt = now - last
            jitter_ms = (now - next_t + self.period) * 1000.0
            fn(dt, jitter_ms)
            last = now
            next_t += self.period
            sleep_time = max(0.0, next_t - time.monotonic())
            time.sleep(sleep_time)
            if duration_s is not None and (time.monotonic() - start) >= duration_s:
                break
