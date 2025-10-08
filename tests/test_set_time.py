from app.main import convert_minutes_to_seconds
import pytest


def test_convert_minutes_positive():
    assert convert_minutes_to_seconds(5) == 300
    assert convert_minutes_to_seconds(0) == 0
    assert convert_minutes_to_seconds(100) == 100 * 60


def test_convert_minutes_negative():
    with pytest.raises(ValueError):
        convert_minutes_to_seconds(-10)
