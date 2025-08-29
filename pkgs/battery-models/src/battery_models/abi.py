from typing import Protocol, Any, Tuple, Mapping


class ModelModule(Protocol):
    def step(self, dt: float, x: Mapping[str, Any], u: Mapping[str, Any]) -> Tuple[dict, dict]:
        """
        Advance state estimate one tick.

        Returns:
            x_next: dict-like state
            y_pred: dict-like outputs/predictions
        """
        ...
