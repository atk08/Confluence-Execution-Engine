from backend.engines.break_of_structure_engine import (
    BreakOfStructureEngine,
)
from backend.engines.swing_detector import SwingDetector
from backend.models.candles import Candle


def test_bullish_break_of_structure():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 105, 100, 104, 1000),   # Swing High (105)
        Candle(104, 103, 101, 102, 1000),
        Candle(102, 104, 102, 103, 1000),
        Candle(103, 104, 102, 106, 1000),   # Close breaks 105
    ]

    swings = SwingDetector.detect_swings(candles)

    print("\nBullish swings:")
    for swing in swings:
        print(swing)

    result = BreakOfStructureEngine.analyze(candles)

    assert result.bullish_break is True
    assert result.bearish_break is False
    assert result.score == 1.0
    assert result.broken_level == 105


def test_bearish_break_of_structure():

    candles = [
        Candle(110, 111, 109, 110, 1000),
        Candle(110, 112, 100, 101, 1000),   # Swing Low (100)
        Candle(101, 111, 103, 109, 1000),
        Candle(109, 110, 104, 108, 1000),
        Candle(108, 109, 99, 99, 1000),     # Close breaks 100
    ]

    swings = SwingDetector.detect_swings(candles)

    print("\nBearish swings:")
    for swing in swings:
        print(swing)

    result = BreakOfStructureEngine.analyze(candles)

    assert result.bullish_break is False
    assert result.bearish_break is True
    assert result.score == 1.0
    assert result.broken_level == 100