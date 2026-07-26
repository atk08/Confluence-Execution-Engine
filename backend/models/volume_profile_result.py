"""
Volume Profile analysis result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class VolumeProfileResult:
    """
    Result of Volume Profile analysis.
    """

    score: float
    bullish: bool
    bearish: bool

    poc: float | None
    value_area_high: float | None
    value_area_low: float | None