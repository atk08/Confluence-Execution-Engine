"""
Anchored VWAP calculation engine.
"""

from backend.models.candles import Candle


class AVWAPCalculator:
    """
    Calculates Anchored VWAP from a list of candles.
    """

    @staticmethod
    def calculate(candles: list[Candle]) -> float:
        if not candles:
            raise ValueError("Candles list cannot be empty.")

        weighted_sum = 0.0
        total_volume = 0.0

        for candle in candles:
            typical_price = (
                candle.high +
                candle.low +
                candle.close
            ) / 3

            weighted_sum += typical_price * candle.volume
            total_volume += candle.volume

        return weighted_sum / total_volume