from fastapi import APIRouter, WebSocket
from typing import List

router = APIRouter()
connections: List[WebSocket] = []

@router.websocket("/ws/logs")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except Exception:
        connections.remove(websocket)
