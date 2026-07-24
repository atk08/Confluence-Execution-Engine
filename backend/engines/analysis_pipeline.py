"""
Institutional Analysis Pipeline.
"""

from backend.engines.avwap_calculator import AVWAPCalculator
from backend.models.candles import Candle


class AnalysisPipeline:
    """
    Coordinates the institutional analysis workflow.
    """

    @staticmethod
    def calculate_avwap(candles: list[Candle]) -> float:
        """
        First stage of the pipeline.
        """
        return AVWAPCalculator.calculate(candles)