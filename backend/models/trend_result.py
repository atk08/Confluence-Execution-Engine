"""
Trend analysis result.
"""

from dataclasses import dataclass

from backend.models.trend import Trend


@dataclass(frozen=True)
class TrendResult:
    """
    Represents the current market trend.
    """

    trend: Trend

    score: float

    confidence: float