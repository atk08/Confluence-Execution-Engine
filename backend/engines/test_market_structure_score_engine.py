"""
Tests for MarketStructureScoreEngine.
"""

from backend.engines.market_structure_score_engine import (
    MarketStructureScoreEngine,
)
from backend.models.candles import Candle
from backend.tests.context_factory import build_context


def test_market_structure_score_defaults():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 101, 1200),
    ]

    context = build_context(candles)

    score = MarketStructureScoreEngine.analyze(context)

    assert score.score >= 0.0
    assert isinstance(score.reasons, list)


def test_market_structure_score_returns_model():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 101, 1200),
    ]

    context = build_context(candles)

    score = MarketStructureScoreEngine.analyze(context)

    assert score is not None
    assert hasattr(score, "score")
    assert hasattr(score, "trend")
    assert hasattr(score, "higher_highs")
    assert hasattr(score, "higher_lows")
    assert hasattr(score, "break_of_structure")
    assert hasattr(score, "change_of_character")
    assert hasattr(score, "displacement")
    assert hasattr(score, "liquidity")