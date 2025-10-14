from ping3 import ping
import socket
import dns.resolver
import time

def check_ping(target, timeout=2):
    """
    Returns latency in seconds (float) or None if unreachable.
    """
    try:
        latency = ping(target, timeout=timeout)
        return latency
    except Exception:
        return None

def check_dns(domain):
    """
    Simple DNS resolution check - returns list of IPs or raises.
    """
    try:
        answers = dns.resolver.resolve(domain, 'A')
        ips = [r.to_text() for r in answers]
        return ips
    except Exception:
        return None

def is_port_open(host, port, timeout=1.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False
