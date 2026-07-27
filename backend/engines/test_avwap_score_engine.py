"""
Tests for AVWAPScoreEngine.
"""

from backend.engines.avwap_score_engine import AVWAPScoreEngine
from backend.models.avwap_result import AVWAPResult


def test_no_avwap():

    result = AVWAPResult(
        bullish=False,
        bearish=False,
        distance_percent=0.0,
        score=0.0,
    )

    score = AVWAPScoreEngine.analyze(result)

    assert score.score == 0.0
    assert score.anchor_quality == 0.0
    assert score.distance == 0.0
    assert score.trend_alignment == 0.0
    assert score.reaction_strength == 0.0
    assert score.confluence == 0.0


def test_avwap_scores_100():

    result = AVWAPResult(
        bullish=True,
        bearish=False,
        distance_percent=0.25,
        score=100.0,
    )

    score = AVWAPScoreEngine.analyze(result)

    assert score.score == 100.0
    assert score.anchor_quality == 20.0
    assert score.distance == 20.0
    assert score.trend_alignment == 20.0
    assert score.reaction_strength == 20.0
    assert score.confluence == 20.0