# monitoring_daemon/monitor.py
import threading
import time
from datetime import datetime
from ping3 import ping  # pip install ping3

# List of IPs or hosts to monitor
hosts_to_monitor = [
    "8.8.8.8",   # Google DNS
    "8.8.4.4",   # Google DNS
    "1.1.1.1"    # Cloudflare DNS
]

def check_host(ip):
    """
    Ping the host and return a log dictionary with status
    """
    latency = ping(ip, timeout=2)  # returns seconds or None
    if latency is None:
        status = "Critical"
        latency_ms = None
    elif latency * 1000 > 100:
        status = "Warning"
        latency_ms = round(latency * 1000, 2)
    else:
        status = "Healthy"
        latency_ms = round(latency * 1000, 2)

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": ip,
        "latency": latency_ms,
        "status": status,
        "action": "ping-test"
    }

def monitor_loop(network_logs, interval=10):
    """
    Main loop to monitor all hosts and append logs to network_logs
    """
    while True:
        for host in hosts_to_monitor:
            log_entry = check_host(host)
            network_logs.append(log_entry)

            # Keep only last 200 logs
            if len(network_logs) > 200:
                network_logs.pop(0)

        time.sleep(interval)

def start_monitoring(network_logs, interval=10):
    """
    Start monitoring in a background thread
    """
    thread = threading.Thread(target=monitor_loop, args=(network_logs, interval), daemon=True)
    thread.start()
async def send_ws_logs(connections, log):
    import asyncio
    import json
    for ws in connections:
        try:
            await ws.send_text(json.dumps(log))
        except:
            connections.remove(ws)

def monitor_loop(network_logs, interval=10, ws_connections=None):
    while True:
        for host in hosts_to_monitor:
            log_entry = check_host(host)
            network_logs.append(log_entry)
            if ws_connections:
                import asyncio
                asyncio.run(send_ws_logs(ws_connections, log_entry))
