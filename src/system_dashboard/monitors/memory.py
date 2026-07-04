import psutil

from system_dashboard.models import MemoryInfo
from system_dashboard.utils import bytes_to_gb


def get_memory_info() -> MemoryInfo:
    mem = psutil.virtual_memory()

    return MemoryInfo(
        total_gb=bytes_to_gb(mem.total),
        used_gb=bytes_to_gb(mem.used),
        free_gb=bytes_to_gb(mem.available),
        percent=mem.percent,
    )
