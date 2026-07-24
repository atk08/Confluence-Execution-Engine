"""
MATH-001: POC Quality Calculator
Version: 1.0
"""

from engines.volume_profile.models import POCQualityInput



def calculate_poc_quality(data: POCQualityInput) -> float:
    """
    Calculates the POC Quality Score.
    """

    score = (
        data.volume_concentration * 0.25
        + data.time_at_price * 0.20
        + data.auction_acceptance * 0.20
        + data.historical_reactions * 0.15
        + data.session_importance * 0.10
        + data.structural_importance * 0.10
    )

    return round(max(0.0, min(score, 100.0)), 1)