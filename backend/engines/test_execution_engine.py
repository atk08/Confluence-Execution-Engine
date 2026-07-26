from backend.engines.execution_engine import ExecutionEngine
from backend.models.candles import Candle
from backend.tests.context_factory import build_context


def test_no_trade_signal():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 101, 99, 100, 1000),
    ]

    context = build_context(candles)

    result = ExecutionEngine.analyze(context)

    assert result.should_trade is False
    assert result.direction == "SELL"
    assert result.trade_score == 0.0


def test_trade_confidence():

    candles = [
        Candle(100, 103, 99, 102, 1000),
        Candle(102, 103, 98, 99, 1000),
        Candle(99, 110, 99, 109, 3000),
    ]

    context = build_context(
        candles,
        bullish_move=True,
    )

    result = ExecutionEngine.analyze(context)

    assert result.trade_score == 30.0
    assert result.confidence == "Low"