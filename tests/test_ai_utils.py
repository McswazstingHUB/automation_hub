from src.ai_utils import ai_assistant


def test_ai_import():
    assert callable(ai_assistant)
