import time
import psutil

def collect_system_state():
    return {
        "timestamp": time.time(),
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "memory_percent": psutil.virtual_memory().percent,
        "active_processes": len(psutil.pids()),
        "observer_mode": "passive"
    }