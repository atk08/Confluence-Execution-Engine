"""
Trend result model.
"""

from dataclasses import dataclass


@dataclass
class TrendResult:
    """
    Result returned by the TrendScore engine.
    """

    score: float
    direction: str
    confidence: float