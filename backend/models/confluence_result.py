"""
Overall Confluence result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ConfluenceResult:
    """
    Final trading confluence score.
    """

    score: float

    trend_score: float
    structure_score: float
    institutional_score: float
    order_block_score: float
    avwap_score: float
    volume_profile_score: float

    bullish: bool
    bearish: bool