"""
Market Structure Score model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MarketStructureScore:
    """
    Represents the overall quality of market structure.
    """

    score: float

    trend: float

    higher_highs: float

    higher_lows: float

    break_of_structure: float

    change_of_character: float

    displacement: float

    liquidity: float

    reasons: list[str]