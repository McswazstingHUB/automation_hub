from dataclasses import dataclass


@dataclass(slots=True)
class DashboardConfig:
    refresh_interval: int = 2
    export_directory: str = "reports"
    use_colors: bool = True
