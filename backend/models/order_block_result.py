"""
Order Block result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderBlockResult:
    """
    Represents an institutional Order Block.
    """

    bullish_block: bool

    bearish_block: bool

    score: float

    block_high: float | None

    block_low: float | None

    candle_index: int | None

    mitigated: bool

    touched: bool

    broken: bool