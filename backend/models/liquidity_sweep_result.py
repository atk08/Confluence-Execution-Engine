"""
Liquidity Sweep result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LiquiditySweepResult:
    """
    Represents a liquidity sweep event.
    """

    bullish_sweep: bool

    bearish_sweep: bool

    score: float

    swept_level: float | None