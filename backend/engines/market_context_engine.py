"""
Market Context Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.market_context import MarketContext
from backend.models.trend import Trend


class MarketContextEngine(AnalysisEngine):
    """
    Determines the overall market context.
    """

    name = "Market Context Engine"

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> MarketContext:

        trend_quality = context.trend.score

        structure_quality = context.structure.score

        bos_quality = context.bos.score

        choch_quality = context.choch.score

        alignment_quality = 20.0

        total = (
            trend_quality
            + structure_quality
            + bos_quality
            + choch_quality
            + alignment_quality
        )

        bullish = context.trend.trend == Trend.BULLISH
        bearish = context.trend.trend == Trend.BEARISH

        strengths = []
        weaknesses = []

        if bullish:
            strengths.append("Bullish trend")

        if bearish:
            strengths.append("Bearish trend")

        if trend_quality < 15:
            weaknesses.append("Weak trend")

        if bos_quality < 10:
            weaknesses.append("Weak break of structure")

        return MarketContext(
            score=min(total, 100.0),
            trend_quality=trend_quality,
            structure_quality=structure_quality,
            bos_quality=bos_quality,
            choch_quality=choch_quality,
            alignment_quality=alignment_quality,
            bullish=bullish,
            bearish=bearish,
            strengths=strengths,
            weaknesses=weaknesses,
            reasons=[
                "Market context evaluated.",
            ],
        )