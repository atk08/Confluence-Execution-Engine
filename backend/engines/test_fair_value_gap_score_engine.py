"""
Tests for FairValueGapScoreEngine.
"""

from backend.engines.fair_value_gap_score_engine import (
    FairValueGapScoreEngine,
)
from backend.models.fair_value_gap_result import FairValueGapResult


def test_no_fair_value_gap():

    result = FairValueGapResult(
        bullish_gap=False,
        bearish_gap=False,
        score=0.0,
        gap_high=None,
        gap_low=None,
        mitigated=False,
        fill_percent=0.0,
        gap_size=0.0,
    )

    score = FairValueGapScoreEngine.analyze(result)

    assert score.score == 0.0
    assert score.freshness == 0.0
    assert score.size == 0.0
    assert score.mitigation == 0.0
    assert score.trend_alignment == 0.0
    assert score.proximity == 0.0


def test_fair_value_gap_scores_100():

    result = FairValueGapResult(
        bullish_gap=True,
        bearish_gap=False,
        score=100.0,
        gap_high=110.0,
        gap_low=100.0,
        mitigated=False,
        fill_percent=0.0,
        gap_size=10.0,
    )

    score = FairValueGapScoreEngine.analyze(result)

    assert score.score == 100.0
    assert score.freshness == 20.0
    assert score.size == 20.0
    assert score.mitigation == 20.0
    assert score.trend_alignment == 20.0
    assert score.proximity == 20.0