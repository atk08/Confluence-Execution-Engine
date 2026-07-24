from backend.engines.swing_detector import Candle, SwingDetector


def test_detects_swing_high():
    assert SwingDetector.is_swing_high(
        Candle(100, 90, 95),
        Candle(110, 95, 100),
        Candle(105, 94, 96),
    )


def test_detects_swing_low():
    assert SwingDetector.is_swing_low(
        Candle(110, 95, 100),
        Candle(108, 90, 94),
        Candle(109, 93, 98),
    )


def test_not_swing_high():
    assert not SwingDetector.is_swing_high(
        Candle(100, 90, 95),
        Candle(99, 91, 94),
        Candle(101, 92, 95),
    )


def test_not_swing_low():
    assert not SwingDetector.is_swing_low(
        Candle(100, 90, 95),
        Candle(101, 91, 96),
        Candle(102, 89, 95),
    )