from src.password_generator import generate_password


def test_password_import():
    assert callable(generate_password)
