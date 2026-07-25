"""
Structure analysis result.
"""

from dataclasses import dataclass

from backend.models.higher_high_result import HigherHighResult
from backend.models.higher_low_result import HigherLowResult
from backend.models.swing_point import SwingPoint
from backend.models.trend import Trend


@dataclass(frozen=True)
class StructureResult:
    """
    Represents the current confirmed market structure.
    """

    score: float

    trend: Trend

    latest_swing_high: SwingPoint | None
    previous_swing_high: SwingPoint | None

    latest_swing_low: SwingPoint | None
    previous_swing_low: SwingPoint | None

    higher_highs: HigherHighResult
    higher_lows: HigherLowResult