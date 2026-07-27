"""
Tests for OrderBlockScoreEngine.
"""

from backend.engines.order_block_score_engine import OrderBlockScoreEngine
from backend.models.order_block_result import OrderBlockResult


def test_no_order_block():

    result = OrderBlockResult(
        bullish_block=False,
        bearish_block=False,
        score=0.0,
        block_high=None,
        block_low=None,
        candle_index=None,
        mitigated=False,
        touched=False,
        broken=False,
    )

    score = OrderBlockScoreEngine.analyze(result)

    assert score.score == 0.0
    assert score.freshness == 0.0
    assert score.displacement == 0.0
    assert score.volume == 0.0
    assert score.trend_alignment == 0.0
    assert score.proximity == 0.0


def test_order_block_scores_100():

    result = OrderBlockResult(
        bullish_block=True,
        bearish_block=False,
        score=100.0,
        block_high=105.0,
        block_low=100.0,
        candle_index=10,
        mitigated=False,
        touched=False,
        broken=False,
    )

    score = OrderBlockScoreEngine.analyze(result)

    assert score.score == 100.0
    assert score.freshness == 20.0
    assert score.displacement == 20.0
    assert score.volume == 20.0
    assert score.trend_alignment == 20.0
    assert score.proximity == 20.0