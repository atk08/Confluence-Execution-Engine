from backend.engines.swing_detector import SwingDetector
from backend.models.candles import Candle


def test_detects_swing_high():
    assert SwingDetector.is_swing_high(
        Candle(open=95, high=100, low=90, close=95, volume=1000),
        Candle(open=100, high=110, low=95, close=100, volume=1200),
        Candle(open=98, high=105, low=94, close=96, volume=900),
    )


def test_detects_swing_low():
    assert SwingDetector.is_swing_low(
        Candle(open=100, high=110, low=95, close=100, volume=1200),
        Candle(open=94, high=108, low=90, close=94, volume=1100),
        Candle(open=98, high=109, low=93, close=98, volume=1000),
    )


def test_not_swing_high():
    assert not SwingDetector.is_swing_high(
        Candle(open=95, high=100, low=90, close=95, volume=1000),
        Candle(open=94, high=99, low=91, close=94, volume=900),
        Candle(open=96, high=101, low=92, close=95, volume=950),
    )


def test_not_swing_low():
    assert not SwingDetector.is_swing_low(
        Candle(open=95, high=100, low=90, close=95, volume=1000),
        Candle(open=96, high=101, low=91, close=96, volume=950),
        Candle(open=95, high=102, low=89, close=95, volume=975),
    )