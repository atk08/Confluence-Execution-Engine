from engines.volume_profile.math004_lvn_quality import calculate_lvn_quality
from engines.volume_profile.models import LVNQualityInput


def test_lvn_quality_high_score():
    data = LVNQualityInput(
        rejection_strength=95,
        breakout_follow_through=90,
        retest_failure=90,
        volume_deficit=85,
        recency=100,
        session_importance=100,
    )

    score = calculate_lvn_quality(data)

    assert score == 91.8


def test_lvn_quality_bounds():
    data = LVNQualityInput(
        rejection_strength=200,
        breakout_follow_through=200,
        retest_failure=200,
        volume_deficit=200,
        recency=200,
        session_importance=200,
    )

    score = calculate_lvn_quality(data)

    assert score == 100.0