"""
Higher High analysis result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class HigherHighResult:
    """
    Result returned by the HigherHighAnalyzer.
    """

    score: float
    total_highs: int
    higher_highs: int
    failed_highs: int