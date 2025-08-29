from collections.abc import Mapping
from typing import Any, Protocol


class ModelModule(Protocol):
    def step(self, dt: float, x: Mapping[str, Any], u: Mapping[str, Any]) -> tuple[dict, dict]:
        """
        Advance state estimate one tick.

        Returns:
            x_next: dict-like state
            y_pred: dict-like outputs/predictions
        """
        ...
