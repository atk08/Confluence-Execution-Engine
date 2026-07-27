"""
Institutional Context model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionalContext:
    """
    Represents the quality of institutional trading context.
    """

    score: float

    order_block_quality: float

    fair_value_gap_quality: float

    liquidity_quality: float

    displacement_quality: float

    alignment_quality: float

    bullish: bool

    bearish: bool

    strengths: list[str]

    weaknesses: list[str]

    reasons: list[str]