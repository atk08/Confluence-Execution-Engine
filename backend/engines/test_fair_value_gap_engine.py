from backend.engines.fair_value_gap_engine import FairValueGapEngine
from backend.models.candles import Candle


def test_no_gap():

    candles = [
        Candle(100, 102, 99, 101, 1000),
        Candle(101, 103, 100, 102, 1000),
        Candle(102, 103, 101, 102, 1000),
    ]

    result = FairValueGapEngine.analyze(candles)

    assert result.bullish_gap is False
    assert result.bearish_gap is False
    assert result.score == 0.0


def test_bullish_gap():

    candles = [
        Candle(100, 102, 99, 101, 1000),
        Candle(101, 107, 101, 106, 2000),
        Candle(108, 110, 108, 109, 1500),
    ]

    result = FairValueGapEngine.analyze(candles)

    assert result.bullish_gap is True
    assert result.bearish_gap is False
    assert result.gap_low == 102
    assert result.gap_high == 108
    assert result.gap_size == 6


def test_bearish_gap():

    candles = [
        Candle(110, 111, 108, 109, 1000),
        Candle(109, 109, 101, 102, 2000),
        Candle(99, 100, 98, 99, 1500),
    ]

    result = FairValueGapEngine.analyze(candles)

    assert result.bearish_gap is True
    assert result.bullish_gap is False
    assert result.gap_high == 108
    assert result.gap_low == 100
    assert result.gap_size == 8