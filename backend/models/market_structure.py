"""
Market Structure model.
"""

from dataclasses import dataclass

from backend.models.swing_point import SwingPoint


@dataclass(frozen=True)
class MarketStructure:
    """
    Represents the current confirmed market structure.
    """

    latest_swing_high: SwingPoint | None
    latest_swing_low: SwingPoint | None

    previous_swing_high: SwingPoint | None
    previous_swing_low: SwingPoint | None