from collections.abc import Mapping
from typing import Any

import numpy as np


class ToyKF:
    """
    Minimal 1D constant-velocity KF example used by the runtime demo.
    State x = [position, velocity]
    u: optional acceleration input 'a'
    y: measured position 'z'
    """

    def __init__(self, dt0: float = 0.02):
        self.Q = np.diag([1e-3, 1e-3])
        self.R = np.array([[1e-2]])
        self.P = np.eye(2) * 1.0
        self.x = np.array([[0.0], [0.0]])
        self.dt = dt0

    def step(self, dt: float, x: Mapping[str, Any], u: Mapping[str, Any]):
        a = float(u.get("a", 0.0))
        z = u.get("z", None)
        F = np.array([[1.0, dt], [0.0, 1.0]])
        B = np.array([[0.5 * dt * dt], [dt]])
        H = np.array([[1.0, 0.0]])

        # Predict
        self.x = F @ self.x + B * a
        self.P = F @ self.P @ F.T + self.Q

        # Update if measurement present
        if z is not None:
            z = np.array([[float(z)]])
            y = z - H @ self.x
            S = H @ self.P @ H.T + self.R
            K = self.P @ H.T @ np.linalg.inv(S)
            self.x = self.x + K @ y
            self.P = (np.eye(2) - K @ H) @ self.P

        x_next = {"pos": float(self.x[0, 0]), "vel": float(self.x[1, 0])}
        y_pred = {"pos": float(self.x[0, 0])}
        return x_next, y_pred
