from backend.engines.analysis_context_builder import (
    AnalysisContextBuilder,
)
from backend.engines.institutional_move_engine import (
    InstitutionalMoveEngine,
)
from backend.models.candles import Candle


def test_no_institutional_move():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 101, 1000),
        Candle(101, 103, 100, 102, 1000),
        Candle(102, 104, 101, 103, 1000),
        Candle(103, 105, 102, 104, 1000),
    ]

    context = AnalysisContextBuilder.build(candles)

    result = InstitutionalMoveEngine.analyze(context)

    assert result.bullish_move is False
    assert result.bearish_move is False
    assert result.score == 0.0