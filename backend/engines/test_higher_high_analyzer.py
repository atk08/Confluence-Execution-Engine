from backend.engines.higher_high_analyzer import HigherHighAnalyzer
from backend.models.candles import Candle


def test_higher_highs():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 105, 99, 104, 1000),   # Swing High
        Candle(104, 101, 97, 99, 1000),
        Candle(99, 108, 98, 107, 1000),    # Swing High
        Candle(107, 102, 96, 100, 1000),
        Candle(100, 112, 99, 111, 1000),   # Swing High
        Candle(111, 103, 98, 101, 1000),
    ]

    score = HigherHighAnalyzer.score(candles)

    assert score == 1.0


def test_no_higher_highs():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 112, 99, 111, 1000),   # Swing High
        Candle(111, 103, 98, 101, 1000),
        Candle(101, 108, 99, 107, 1000),   # Swing High
        Candle(107, 102, 98, 100, 1000),
        Candle(100, 105, 99, 104, 1000),   # Swing High
        Candle(104, 101, 98, 100, 1000),
    ]

    score = HigherHighAnalyzer.score(candles)

    assert score == 0.0


def test_not_enough_swing_highs():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 100, 99, 100, 1000),
    ]

    score = HigherHighAnalyzer.score(candles)

    assert score == 0.5