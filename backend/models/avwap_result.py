"""
Anchored VWAP analysis result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AVWAPResult:
    """
    Result of Anchored VWAP analysis.
    """

    score: float
    bullish: bool
    bearish: bool
    distance_percent: float