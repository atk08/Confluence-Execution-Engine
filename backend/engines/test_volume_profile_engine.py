"""
Tests for VolumeProfileEngine.
"""

from backend.engines.volume_profile_engine import VolumeProfileEngine
from backend.models.candles import Candle
from backend.models.volume_profile_result import VolumeProfileResult


def build_candle(
    open_price,
    high,
    low,
    close,
    volume,
):
    return Candle(
        open=open_price,
        high=high,
        low=low,
        close=close,
        volume=volume,
    )


def test_empty_candles():

    result = VolumeProfileEngine.analyze([])

    assert isinstance(result, VolumeProfileResult)
    assert result.score == 0.0
    assert result.poc is None
    assert result.value_area_high is None
    assert result.value_area_low is None
    assert result.bullish is False
    assert result.bearish is False


def test_volume_profile_returns_result():

    candles = [
        build_candle(100, 102, 99, 101, 1000),
        build_candle(101, 104, 100, 103, 2500),
        build_candle(103, 105, 102, 104, 1800),
        build_candle(104, 106, 103, 105, 1500),
    ]

    result = VolumeProfileEngine.analyze(candles)

    assert isinstance(result, VolumeProfileResult)
    assert result.poc is not None
    assert result.value_area_high is not None
    assert result.value_area_low is not None
    assert 0.0 <= result.score <= 100.0