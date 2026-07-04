import os
import psutil

from system_dashboard.models import CPUInfo


def get_cpu_info() -> CPUInfo:
    usage = None

    try:
        usage = psutil.cpu_percent(interval=0.2)
    except (PermissionError, FileNotFoundError, OSError):
        pass

    return CPUInfo(
        cores=os.cpu_count() or 0,
        usage_percent=usage if usage is not None else -1.0,
    )
