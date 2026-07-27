"""
Anchored VWAP Result Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.engines.avwap_calculator import AVWAPCalculator
from backend.models.avwap_result import AVWAPResult
from backend.models.candles import Candle


class AVWAPResultEngine(AnalysisEngine):
    """
    Builds an AVWAPResult from candle data.
    """

    name = "AVWAP Result"

    @classmethod
    def analyze(
        cls,
        candles: list[Candle],
    ) -> AVWAPResult:

        if len(candles) < 2:
            return AVWAPResult(
                score=0.0,
                bullish=False,
                bearish=False,
                distance_percent=0.0,
            )

        avwap = AVWAPCalculator.calculate(candles)

        current_price = candles[-1].close

        distance_percent = (
            abs(current_price - avwap)
            / avwap
            * 100
        )

        bullish = current_price > avwap
        bearish = current_price < avwap

        score = max(
            0.0,
            min(
                100.0,
                100.0 - (distance_percent * 20),
            ),
        )

        return AVWAPResult(
            score=score,
            bullish=bullish,
            bearish=bearish,
            distance_percent=distance_percent,
        )