"""
Liquidity Score model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LiquidityScore:
    """
    Represents the quality score of a liquidity sweep.
    """

    score: float

    sweep_strength: float

    location: float

    trend_alignment: float

    continuation_probability: float

    freshness: float

    reasons: list[str]