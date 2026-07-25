"""
Break Of Structure result model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BreakOfStructureResult:
    """
    Result of BOS analysis.
    """

    bullish_break: bool
    bearish_break: bool
    score: float
    broken_level: float | None