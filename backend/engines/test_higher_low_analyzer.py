from backend.engines.higher_low_analyzer import HigherLowAnalyzer
from backend.models.candles import Candle


def test_higher_lows():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 103, 95, 102, 1000),
        Candle(102, 104, 97, 103, 1000),  # Swing Low = 95
        Candle(103, 106, 100, 105, 1000),
        Candle(105, 107, 99, 106, 1000),
        Candle(106, 109, 101, 108, 1000),  # Swing Low = 99
        Candle(108, 110, 103, 109, 1000),
    ]

    result = HigherLowAnalyzer.analyze(candles)

    assert result.score == 1.0
    assert result.total_lows == 2
    assert result.higher_lows == 1
    assert result.failed_lows == 0


def test_lower_lows():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 103, 98, 102, 1000),
        Candle(102, 104, 96, 103, 1000),  # Swing Low = 96
        Candle(103, 106, 100, 105, 1000),
        Candle(105, 107, 94, 106, 1000),  # Swing Low = 94
        Candle(106, 109, 101, 108, 1000),
        Candle(108, 110, 103, 109, 1000),
    ]

    result = HigherLowAnalyzer.analyze(candles)

    assert result.score == 0.0
    assert result.total_lows == 2
    assert result.higher_lows == 0
    assert result.failed_lows == 1