import os
import platform
import subprocess

def flush_dns():
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.run(["ipconfig", "/flushdns"], check=True)
        elif system == "Darwin":
            # macOS
            subprocess.run(["sudo", "dscacheutil", "-flushcache"], check=True)
            subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"], check=True)
        else:
            # Linux (systemd-resolved)
            subprocess.run(["sudo", "systemd-resolve", "--flush-caches"], check=True)
    except Exception as e:
        return {"success": False, "error": str(e)}
    return {"success": True}

def restart_adapter(adapter_name=None):
    system = platform.system()
    try:
        if system == "Windows":
            # requires admin - toggle a named adapter; fallback to using Wi-Fi name 'Wi-Fi'
            iface = adapter_name or "Wi-Fi"
            subprocess.run(["netsh", "interface", "set", "interface", iface, "disable"], check=True)
            subprocess.run(["netsh", "interface", "set", "interface", iface, "enable"], check=True)
        elif system == "Darwin":
            # macOS: use networksetup (adapter_name should be like "Wi-Fi")
            iface = adapter_name or "Wi-Fi"
            subprocess.run(["sudo", "ifconfig", iface, "down"], check=True)
            subprocess.run(["sudo", "ifconfig", iface, "up"], check=True)
        else:
            # Linux: try to bring down/up interface (requires sudo)
            if adapter_name:
                subprocess.run(["sudo", "ip", "link", "set", adapter_name, "down"], check=True)
                subprocess.run(["sudo", "ip", "link", "set", adapter_name, "up"], check=True)
            else:
                # fallback: restart NetworkManager if available
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"], check=True)
    except Exception as e:
        return {"success": False, "error": str(e)}
    return {"success": True}
