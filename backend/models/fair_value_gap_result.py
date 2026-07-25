"""
Fair Value Gap result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class FairValueGapResult:
    """
    Represents a Fair Value Gap.
    """

    bullish_gap: bool

    bearish_gap: bool

    score: float

    gap_high: float | None

    gap_low: float | None

    mitigated: bool

    fill_percent: float

    gap_size: float