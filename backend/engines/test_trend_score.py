from backend.engines.trend_score import TrendScore
from backend.models.candles import Candle
from backend.models.trend import Trend


def test_bullish_trend():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 102, 1000),
        Candle(102, 104, 101, 104, 1000),
    ]

    result = TrendScore.calculate(candles)

    assert result.trend == Trend.BULLISH
    assert result.score == 1.0


def test_bearish_trend():

    candles = [
        Candle(104, 105, 103, 104, 1000),
        Candle(104, 104, 100, 101, 1000),
        Candle(101, 102, 98, 99, 1000),
    ]

    result = TrendScore.calculate(candles)

    assert result.trend == Trend.BEARISH
    assert result.score == 0.0


def test_ranging_trend():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 98, 100, 1000),
    ]

    result = TrendScore.calculate(candles)

    assert result.trend == Trend.RANGING
    assert result.score == 0.5