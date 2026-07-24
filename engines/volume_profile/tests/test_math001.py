from engines.volume_profile.math001_poc_quality import (
    POCQualityInput,
    calculate_poc_quality,
)


def test_all_100():
    data = POCQualityInput(
        volume_concentration=100,
        time_at_price=100,
        auction_acceptance=100,
        historical_reactions=100,
        session_importance=100,
        structural_importance=100,
    )

    assert calculate_poc_quality(data) == 100.0


def test_all_50():
    data = POCQualityInput(
        volume_concentration=50,
        time_at_price=50,
        auction_acceptance=50,
        historical_reactions=50,
        session_importance=50,
        structural_importance=50,
    )

    assert calculate_poc_quality(data) == 50.0