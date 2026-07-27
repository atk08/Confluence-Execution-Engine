"""
Tests for LiquidityScoreEngine.
"""

from backend.engines.liquidity_score_engine import LiquidityScoreEngine
from backend.models.liquidity_sweep_result import LiquiditySweepResult


def test_no_liquidity_sweep():

    result = LiquiditySweepResult(
        bullish_sweep=False,
        bearish_sweep=False,
        score=0.0,
        swept_level=None,
    )

    score = LiquidityScoreEngine.analyze(result)

    assert score.score == 0.0
    assert score.sweep_strength == 0.0
    assert score.location == 0.0
    assert score.trend_alignment == 0.0
    assert score.continuation_probability == 0.0
    assert score.freshness == 0.0


def test_liquidity_scores_100():

    result = LiquiditySweepResult(
        bullish_sweep=True,
        bearish_sweep=False,
        score=100.0,
        swept_level=100.0,
    )

    score = LiquidityScoreEngine.analyze(result)

    assert score.score == 100.0
    assert score.sweep_strength == 20.0
    assert score.location == 20.0
    assert score.trend_alignment == 20.0
    assert score.continuation_probability == 20.0
    assert score.freshness == 20.0