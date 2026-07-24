from backend.engines.higher_high_analyzer import HigherHighAnalyzer
from backend.models.candles import Candle


def test_all_higher_highs():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 103, 99, 102, 1000),
        Candle(102, 105, 101, 104, 1000),
    ]

    score = HigherHighAnalyzer.score(candles)

    assert score == 1.0


def test_no_higher_highs():

    candles = [
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 104, 100, 102, 1000),
        Candle(102, 103, 99, 100, 1000),
    ]

    score = HigherHighAnalyzer.score(candles)

    assert score == 0.0


def test_partial_higher_highs():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 103, 99, 102, 1000),
        Candle(102, 102, 100, 101, 1000),
    ]

    score = HigherHighAnalyzer.score(candles)

    assert score == 0.5