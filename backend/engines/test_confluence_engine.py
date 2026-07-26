from backend.engines.confluence_engine import ConfluenceEngine
from backend.models.candles import Candle
from backend.tests.context_factory import build_context


def test_empty_confluence():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 101, 99, 100, 1000),
    ]

    context = build_context(candles)

    result = ConfluenceEngine.analyze(context)

    assert result.score == 0.0
    assert result.bullish is False
    assert result.bearish is True


def test_bullish_confluence():

    candles = [
        Candle(100, 103, 99, 102, 1000),
        Candle(102, 103, 98, 99, 1000),
        Candle(99, 110, 99, 109, 3000),
    ]

    context = build_context(
        candles,
        bullish_move=True,
    )

    result = ConfluenceEngine.analyze(context)

    assert result.institutional_score == 100.0
    assert result.score == 30.0