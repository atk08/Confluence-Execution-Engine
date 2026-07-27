from backend.engines.atr_engine import ATREngine
from backend.models.candles import Candle
from backend.tests.context_factory import build_context


def test_atr_returns_positive_value():

    candles = [
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 108, 103, 107, 1200),
        Candle(107, 112, 106, 111, 1400),
    ]

    context = build_context(candles)

    result = ATREngine.analyze(context)

    assert result.value > 0
    assert result.period == 14


def test_atr_with_insufficient_data():

    candles = [
        Candle(100, 101, 99, 100, 1000),
    ]

    context = build_context(candles)

    result = ATREngine.analyze(context)

    assert result.value == 0.0
    assert result.period == 14