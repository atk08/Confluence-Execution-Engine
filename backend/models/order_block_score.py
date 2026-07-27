"""
Order Block Score model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderBlockScore:
    """
    Represents the quality of an order block.
    """

    score: float

    freshness: float

    displacement: float

    volume: float

    trend_alignment: float

    proximity: float

    reasons: list[str]