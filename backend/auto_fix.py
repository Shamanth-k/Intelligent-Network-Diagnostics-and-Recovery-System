# auto_fix.py
import subprocess
import platform

def flush_dns():
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.run(["ipconfig", "/flushdns"], check=True)
        elif system == "Linux":
            subprocess.run(["sudo", "systemd-resolve", "--flush-caches"], check=True)
        elif system == "Darwin":  # macOS
            subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"], check=True)
        else:
            return {"status": "error", "message": f"Unsupported OS: {system}"}

        return {"status": "success", "message": "DNS cache flushed successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def restart_network_adapter():
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "disabled"], check=True)
            subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "enabled"], check=True)
        elif system == "Linux":
            subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"], check=True)
        elif system == "Darwin":
            subprocess.run(["sudo", "ifconfig", "en0", "down"], check=True)
            subprocess.run(["sudo", "ifconfig", "en0", "up"], check=True)
        else:
            return {"status": "error", "message": f"Unsupported OS: {system}"}

        return {"status": "success", "message": "Network adapter restarted successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
