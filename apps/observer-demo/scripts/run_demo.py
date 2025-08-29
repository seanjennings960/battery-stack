import time

from battery_data.schemas import RuntimeLogRecord
from battery_models.toy_kf import ToyKF
from battery_runtime.adapters import StdOutSink, SyntheticSource
from battery_runtime.scheduler import FixedRate


def main():
    model = ToyKF()
    src = SyntheticSource()
    sink = StdOutSink()
    state = {}

    def tick(dt: float, jitter_ms: float):
        u = src.read() or {}
        x_next, y_pred = model.step(dt, state, u)
        rec = RuntimeLogRecord(
            t_wall=time.time(),
            t_source=u.get("t_source"),
            dt=dt,
            jitter_ms=jitter_ms,
            u=u,
            x=x_next,
            y_pred=y_pred,
            residuals={"pos": (u.get("z", 0.0) - y_pred["pos"]) if "z" in u else 0.0},
        )
        sink.write(rec.model_dump())

    FixedRate(hz=50).run(tick, duration_s=2.0)


if __name__ == "__main__":
    main()
