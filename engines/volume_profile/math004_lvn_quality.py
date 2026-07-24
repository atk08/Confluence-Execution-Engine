from engines.volume_profile.models import LVNQualityInput


def calculate_lvn_quality(data: LVNQualityInput) -> float:
    """
    Calculate the quality score of a Low Volume Node (LVN).

    Returns a score between 0 and 100.
    """

    score = (
        data.rejection_strength * 0.30
        + data.breakout_follow_through * 0.25
        + data.retest_failure * 0.20
        + data.volume_deficit * 0.15
        + data.recency * 0.05
        + data.session_importance * 0.05
    )

    return round(max(0.0, min(score, 100.0)), 1)