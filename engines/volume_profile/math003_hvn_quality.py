from engines.volume_profile.models import HVNQualityInput


def calculate_hvn_quality(data: HVNQualityInput) -> float:
    """
    Calculate the quality score of a High Volume Node (HVN).

    Returns a score between 0 and 100.
    """

    score = (
        data.volume_concentration * 0.30
        + data.time_at_price * 0.20
        + data.historical_reactions * 0.20
        + data.distance_from_poc * 0.15
        + data.recency * 0.10
        + data.session_importance * 0.05
    )

    return round(max(0.0, min(score, 100.0)), 1)