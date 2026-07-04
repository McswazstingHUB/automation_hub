import psutil

from system_dashboard.models import DiskInfo
from system_dashboard.utils import bytes_to_gb


def get_disk_info() -> DiskInfo:
    disk = psutil.disk_usage("/")

    return DiskInfo(
        total_gb=bytes_to_gb(disk.total),
        used_gb=bytes_to_gb(disk.used),
        free_gb=bytes_to_gb(disk.free),
        percent=disk.percent,
    )
