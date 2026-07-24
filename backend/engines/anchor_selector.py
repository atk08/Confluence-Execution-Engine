"""
Anchor selection engine.
"""

from backend.engines.swing_detector import Candle


class AnchorSelector:
    """
    Selects the strongest swing highs and lows.
    """

    @staticmethod
    def select_high_anchor(swings: list[Candle]) -> Candle:
        """
        Returns the swing with the highest high.
        """
        return max(swings, key=lambda candle: candle.high)

    @staticmethod
    def select_low_anchor(swings: list[Candle]) -> Candle:
        """
        Returns the swing with the lowest low.
        """
        return min(swings, key=lambda candle: candle.low)