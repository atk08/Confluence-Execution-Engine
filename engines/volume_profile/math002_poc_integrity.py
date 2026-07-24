"""
MATH-002: POC Integrity Calculator
Version: 1.0
"""

from engines.volume_profile.models import POCIntegrityInput


def calculate_poc_integrity(data: POCIntegrityInput) -> float:
    """
    Calculates the integrity of a Point of Control.
    """

    score = 100.0

    score -= data.revisits * 5.0
    score -= data.penetration_penalty
    score -= data.acceptance_penalty

    score += data.rejection_bonus
    score += data.freshness_bonus

    return round(max(0.0, min(score, 100.0)), 1)