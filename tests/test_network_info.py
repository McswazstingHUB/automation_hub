from src.network_info import show_network_info


def test_network_import():
    assert callable(show_network_info)
