"""
Fair Value Gap Score model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class FairValueGapScore:
    """
    Represents the quality score of a Fair Value Gap.
    """

    score: float

    freshness: float

    size: float

    mitigation: float

    trend_alignment: float

    proximity: float

    reasons: list[str]