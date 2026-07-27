"""
Tests for VolumeProfileScoreEngine.
"""

from backend.engines.volume_profile_score_engine import (
    VolumeProfileScoreEngine,
)
from backend.models.volume_profile_result import VolumeProfileResult


def test_no_volume_profile():

    result = VolumeProfileResult(
        bullish=False,
        bearish=False,
        poc=0.0,
        value_area_high=0.0,
        value_area_low=0.0,
        score=0.0,
    )

    score = VolumeProfileScoreEngine.analyze(result)

    assert score.score == 0.0
    assert score.poc_quality == 0.0
    assert score.value_area == 0.0
    assert score.hvn_lvn == 0.0
    assert score.reaction_strength == 0.0
    assert score.confluence == 0.0


def test_volume_profile_scores_100():

    result = VolumeProfileResult(
        bullish=True,
        bearish=False,
        poc=100.0,
        value_area_high=105.0,
        value_area_low=95.0,
        score=100.0,
    )

    score = VolumeProfileScoreEngine.analyze(result)

    assert score.score == 100.0
    assert score.poc_quality == 20.0
    assert score.value_area == 20.0
    assert score.hvn_lvn == 20.0
    assert score.reaction_strength == 20.0
    assert score.confluence == 20.0