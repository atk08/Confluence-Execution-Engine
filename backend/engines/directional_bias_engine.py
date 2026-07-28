"""
Directional Bias Engine.

Determines bullish vs bearish alignment.
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_context import AnalysisContext

from backend.models.directional_bias import (
    DirectionalBias,
)


class DirectionalBiasEngine(AnalysisEngine):

    name = "Directional Bias"


    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> DirectionalBias:


        bullish_score = 0.0
        bearish_score = 0.0

        reasons = []


        #
        # Trend
        #

        if context.trend:

            trend_text = str(
                context.trend
            ).lower()


            if "bull" in trend_text:

                bullish_score += 20

                reasons.append(
                    "Bullish trend alignment."
                )


            elif "bear" in trend_text:

                bearish_score += 20

                reasons.append(
                    "Bearish trend alignment."
                )


        #
        # Liquidity
        #

        if context.liquidity:

            if context.liquidity.bullish_sweep:

                bullish_score += 20

                reasons.append(
                    "Bullish liquidity sweep."
                )


            if context.liquidity.bearish_sweep:

                bearish_score += 20

                reasons.append(
                    "Bearish liquidity sweep."
                )


        #
        # Institutional Move
        #

        if context.institutional_move:

            if context.institutional_move.bullish_move:

                bullish_score += 20

                reasons.append(
                    "Bullish institutional move."
                )


            if context.institutional_move.bearish_move:

                bearish_score += 20

                reasons.append(
                    "Bearish institutional move."
                )


        #
        # FVG
        #

        if context.fvg:

            if context.fvg.bullish_gap:

                bullish_score += 20

                reasons.append(
                    "Bullish FVG."
                )


            if context.fvg.bearish_gap:

                bearish_score += 20

                reasons.append(
                    "Bearish FVG."
                )


        #
        # Final Bias
        #

        if bullish_score > bearish_score:

            bias = "BULLISH"


        elif bearish_score > bullish_score:

            bias = "BEARISH"


        else:

            bias = "NEUTRAL"


        return DirectionalBias(
            bullish_score=bullish_score,
            bearish_score=bearish_score,
            bias=bias,
            reasons=reasons,
        )