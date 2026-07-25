from backend.engines.trend_engine import TrendEngine
from backend.models.candles import Candle
from backend.models.trend import Trend


def test_bullish_trend():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 101, 97, 99, 1000),
        Candle(99, 108, 100, 107, 1000),
        Candle(107, 104, 98, 105, 1000),
        Candle(105, 112, 101, 111, 1000),
        Candle(111, 106, 102, 108, 1000),
    ]

    result = TrendEngine.analyze(candles)

    assert result.trend == Trend.BULLISH
    assert result.confidence > 0.60


def test_not_bullish_trend():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 112, 99, 111, 1000),
        Candle(111, 103, 98, 101, 1000),
        Candle(101, 108, 99, 107, 1000),
        Candle(107, 102, 98, 100, 1000),
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 101, 98, 100, 1000),
    ]

    result = TrendEngine.analyze(candles)

    assert result.trend != Trend.BULLISH