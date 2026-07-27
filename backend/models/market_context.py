"""
Market Context model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MarketContext:
    """
    Represents the overall market context.
    """

    score: float

    trend_quality: float

    structure_quality: float

    bos_quality: float

    choch_quality: float

    alignment_quality: float

    bullish: bool

    bearish: bool

    strengths: list[str]

    weaknesses: list[str]

    reasons: list[str]