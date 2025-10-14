# Optional Pydantic model definitions (if you want to expand)
from pydantic import BaseModel
from typing import Optional

class NetworkLog(BaseModel):
    timestamp: str
    target: str
    latency: Optional[float] = None
    status: str
    details: Optional[str] = None
