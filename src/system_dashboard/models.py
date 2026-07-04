from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class CPUInfo:
    cores: int
    usage_percent: float


@dataclass(slots=True)
class MemoryInfo:
    total_gb: float
    used_gb: float
    free_gb: float
    percent: float


@dataclass(slots=True)
class DiskInfo:
    total_gb: float
    used_gb: float
    free_gb: float
    percent: float


@dataclass(slots=True)
class NetworkInfo:
    bytes_sent: Optional[int]
    bytes_recv: Optional[int]


@dataclass(slots=True)
class DashboardData:
    cpu: CPUInfo
    memory: MemoryInfo
    disk: DiskInfo
    network: Optional[NetworkInfo] = None
