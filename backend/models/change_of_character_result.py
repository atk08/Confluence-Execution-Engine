"""
Change of Character result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ChangeOfCharacterResult:
    """
    Represents a Change of Character (CHoCH).
    """

    bullish_choch: bool

    bearish_choch: bool

    score: float

    broken_level: float | None