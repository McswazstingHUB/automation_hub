import psutil

from system_dashboard.models import NetworkInfo


def get_network_info() -> NetworkInfo:
    try:
        stats = psutil.net_io_counters()

        return NetworkInfo(
            bytes_sent=stats.bytes_sent,
            bytes_recv=stats.bytes_recv,
        )

    except (PermissionError, FileNotFoundError, OSError):
        return NetworkInfo(
            bytes_sent=-1,
            bytes_recv=-1,
        )
