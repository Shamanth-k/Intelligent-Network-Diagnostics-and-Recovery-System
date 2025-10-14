from fastapi import APIRouter
from pymongo import MongoClient

router = APIRouter(prefix="/api/metrics", tags=["Metrics"])
client = MongoClient("mongodb://localhost:27017/")
db = client["intellinet"]
logs_collection = db["network_logs"]

@router.get("/status")
def get_summary():
    logs = list(logs_collection.find({}, {"_id": 0}))
    total = len(logs)
    healthy = len([l for l in logs if l.get("status") == "HEALTHY"])
    critical = len([l for l in logs if l.get("status") == "UNREACHABLE"])
    warning = len([l for l in logs if l.get("status") == "HIGH_LATENCY"])
    return {"total": total, "healthy": healthy, "warning": warning, "critical": critical}
