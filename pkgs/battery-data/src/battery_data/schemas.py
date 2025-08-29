from pydantic import BaseModel, Field
from typing import Any, Dict, Optional


class RuntimeLogRecord(BaseModel):
    t_wall: float = Field(..., description="Wall-clock timestamp (s)")
    t_source: Optional[float] = Field(None, description="Source timestamp if available")
    dt: float
    jitter_ms: float
    u: Dict[str, Any]
    x: Dict[str, Any]
    y_pred: Dict[str, Any]
    residuals: Optional[Dict[str, Any]] = None
