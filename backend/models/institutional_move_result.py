"""
Institutional Move result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionalMoveResult:
    """
    Represents a confirmed institutional displacement.
    """

    bullish_move: bool

    bearish_move: bool

    score: float

    has_bos: bool

    has_choch: bool

    has_fvg: bool

    displacement: bool