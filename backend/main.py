# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auto_fix import flush_dns, restart_network_adapter
from monitoring_daemon.monitor import start_monitoring  # monitoring_daemon is now inside backend/
from typing import List
from datetime import datetime
import threading
from routes.ws import router as ws_router




app = FastAPI(title="IntelliNet Backend")

# Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for logs (replace with MongoDB later)
network_logs = []

app.include_router(ws_router)

# --- Home Route ---
@app.get("/")
def home():
    return {"message": "IntelliNet Backend Running 🚀"}

# --- Auto Fix Routes ---
@app.post("/api/fix/flush-dns")
def fix_dns():
    result = flush_dns()
    network_logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": "flush-dns",
        "result": result.get("status", "Unknown"),
        "status": "Info"
    })
    return result

@app.post("/api/fix/restart-adapter")
def fix_adapter():
    result = restart_network_adapter()
    network_logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": "restart-adapter",
        "result": result.get("status", "Unknown"),
        "status": "Info"
    })
    return result

# --- Metrics Route ---
@app.get("/api/metrics/status")
def get_metrics():
    healthy = sum(1 for log in network_logs if log.get("status") == "Healthy")
    warning = sum(1 for log in network_logs if log.get("status") == "Warning")
    critical = sum(1 for log in network_logs if log.get("status") == "Critical")
    info = sum(1 for log in network_logs if log.get("status") == "Info")
    return {"healthy": healthy, "warning": warning, "critical": critical, "info": info}

# --- Logs Route ---
@app.get("/api/logs")
def get_logs(limit: int = 50):
    return {"logs": network_logs[-limit:]}

# --- Start monitoring daemon in background ---
def start_background_monitor():
    # Pass network_logs so monitor.py can append logs directly
    start_monitoring(network_logs)

# Run monitoring in a separate thread so it doesn’t block FastAPI
threading.Thread(target=start_background_monitor, daemon=True).start()

# --- Test logs for initial data ---
network_logs.append({
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "ip": "8.8.8.8",
    "latency": 20,
    "status": "Healthy",
    "action": "ping-test"
})
network_logs.append({
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "ip": "8.8.4.4",
    "latency": 120,
    "status": "Warning",
    "action": "ping-test"
})
