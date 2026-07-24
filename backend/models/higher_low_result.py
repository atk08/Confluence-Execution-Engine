"""
Higher Low analysis result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class HigherLowResult:
    """
    Result returned by the HigherLowAnalyzer.
    """

    score: float
    total_lows: int
    higher_lows: int
    failed_lows: int