from fastapi import APIRouter, Body, HTTPException
from pymongo import MongoClient
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/api/logs", tags=["Logs"])

# MongoDB client - adjust URI if needed
client = MongoClient("mongodb://localhost:27017/")
db = client["intellinet"]
logs_collection = db["network_logs"]

class LogItem(BaseModel):
    target: str
    latency: Optional[float] = None
    status: str
    details: Optional[str] = None

@router.post("/")
def add_log(log: LogItem = Body(...)):
    doc = log.dict()
    doc["timestamp"] = datetime.utcnow().isoformat()
    logs_collection.insert_one(doc)
    return {"status": "success", "message": "Log saved"}

@router.get("/")
def get_logs(limit: int = 100):
    docs = list(logs_collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(limit))
    return {"logs": docs}
