from engines.volume_profile.math003_hvn_quality import calculate_hvn_quality
from engines.volume_profile.models import HVNQualityInput


def test_hvn_quality_high_score():
    data = HVNQualityInput(
        volume_concentration=95,
        time_at_price=90,
        historical_reactions=85,
        distance_from_poc=90,
        recency=95,
        session_importance=100,
    )

    score = calculate_hvn_quality(data)

    assert score == 91.5


def test_hvn_quality_bounds():
    data = HVNQualityInput(
        volume_concentration=200,
        time_at_price=200,
        historical_reactions=200,
        distance_from_poc=200,
        recency=200,
        session_importance=200,
    )

    score = calculate_hvn_quality(data)

    assert score == 100.0