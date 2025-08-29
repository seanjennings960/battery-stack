from typing import Any

from pydantic import BaseModel, Field


class RuntimeLogRecord(BaseModel):
    t_wall: float = Field(..., description="Wall-clock timestamp (s)")
    t_source: float | None = Field(None, description="Source timestamp if available")
    dt: float
    jitter_ms: float
    u: dict[str, Any]
    x: dict[str, Any]
    y_pred: dict[str, Any]
    residuals: dict[str, Any] | None = None
