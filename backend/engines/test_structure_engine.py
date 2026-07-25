from backend.engines.structure_engine import StructureEngine
from backend.models.candles import Candle
from backend.models.trend import Trend


def test_bullish_structure():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 101, 97, 99, 1000),
        Candle(99, 108, 100, 107, 1000),
        Candle(107, 104, 98, 105, 1000),
        Candle(105, 112, 101, 111, 1000),
        Candle(111, 106, 102, 108, 1000),
    ]

    result = StructureEngine.analyze(candles)

    assert result.trend == Trend.BULLISH
    assert result.score > 0.60

    assert result.higher_highs is not None
    assert result.higher_lows is not None

    assert result.latest_swing_high is not None
    assert result.latest_swing_low is not None


def test_non_bullish_structure():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 112, 99, 111, 1000),
        Candle(111, 103, 98, 101, 1000),
        Candle(101, 108, 99, 107, 1000),
        Candle(107, 102, 98, 100, 1000),
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 101, 98, 100, 1000),
    ]

    result = StructureEngine.analyze(candles)

    assert result.trend != Trend.BULLISH
    assert result.score < 0.60

    assert result.higher_highs is not None
    assert result.higher_lows is not None