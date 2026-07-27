"""
Confluence Score V2 model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ConfluenceScoreV2:
    """
    Final weighted confluence score.
    """

    score: float

    market_structure: float

    volume_profile: float

    avwap: float

    order_block: float

    fair_value_gap: float

    liquidity: float

    reasons: list[str]