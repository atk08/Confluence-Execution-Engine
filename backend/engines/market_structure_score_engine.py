"""
Market Structure Score Engine.

Calculates a weighted market structure score.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.market_structure_score import MarketStructureScore
from backend.models.trend import Trend


class MarketStructureScoreEngine(AnalysisEngine):
    """
    Calculates an overall market structure score.
    """

    name = "Market Structure Score"

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> MarketStructureScore:

        trend = 0.0
        higher_highs = 0.0
        higher_lows = 0.0
        break_of_structure = 0.0
        change_of_character = 0.0
        displacement = 0.0
        liquidity = 0.0

        reasons: list[str] = []

        #
        # Trend
        #

        if (
            context.trend is not None
            and context.trend.trend == Trend.BULLISH
        ):
            trend = 20.0
            reasons.append("Bullish trend detected.")

        #
        # Higher Highs
        #

        if (
            context.structure is not None
            and context.structure.higher_highs.score > 0
        ):
            higher_highs = 15.0
            reasons.append("Higher highs confirmed.")

        #
        # Higher Lows
        #

        if (
            context.structure is not None
            and context.structure.higher_lows.score > 0
        ):
            higher_lows = 15.0
            reasons.append("Higher lows confirmed.")

        #
        # Break of Structure
        #

        if (
            context.bos is not None
            and (
                context.bos.bullish_break
                or context.bos.bearish_break
            )
        ):
            break_of_structure = 15.0
            reasons.append("Break of Structure confirmed.")

        #
        # Change of Character
        #

        if (
            context.choch is not None
            and (
                context.choch.bullish_choch
                or context.choch.bearish_choch
            )
        ):
            change_of_character = 10.0
            reasons.append("Change of Character confirmed.")

        #
        # Institutional Move
        #

        if (
            context.institutional_move is not None
            and context.institutional_move.displacement
        ):
            displacement = 15.0
            reasons.append("Institutional displacement detected.")

        #
        # Liquidity Sweep
        #

        if (
            context.liquidity is not None
            and (
                context.liquidity.bullish_sweep
                or context.liquidity.bearish_sweep
            )
        ):
            liquidity = 10.0
            reasons.append("Liquidity sweep detected.")

        score = (
            trend
            + higher_highs
            + higher_lows
            + break_of_structure
            + change_of_character
            + displacement
            + liquidity
        )

        return MarketStructureScore(
            score=score,
            trend=trend,
            higher_highs=higher_highs,
            higher_lows=higher_lows,
            break_of_structure=break_of_structure,
            change_of_character=change_of_character,
            displacement=displacement,
            liquidity=liquidity,
            reasons=reasons,
        )