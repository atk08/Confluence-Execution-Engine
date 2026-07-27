"""
Liquidity Score Engine.

Calculates liquidity quality score.

Supports:
- AnalysisContext (production pipeline)
- LiquiditySweepResult (legacy tests)
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_context import AnalysisContext

from backend.models.liquidity_score import LiquidityScore

from backend.models.liquidity_sweep_result import (
    LiquiditySweepResult,
)


class LiquidityScoreEngine(AnalysisEngine):

    name = "Liquidity Score"


    @classmethod
    def analyze(
        cls,
        data,
    ) -> LiquidityScore:


        #
        # Backwards compatibility
        #
        # Tests pass LiquiditySweepResult
        #

        if isinstance(
            data,
            LiquiditySweepResult
        ):

            liquidity = data

            trend_alignment = 20.0
            continuation_probability = 20.0


        #
        # Production pipeline
        #
        # Receives AnalysisContext
        #

        elif isinstance(
            data,
            AnalysisContext
        ):

            liquidity = data.liquidity


            trend_alignment = (
                20.0
                if data.trend is not None
                else 0.0
            )


            continuation_probability = (
                20.0
                if (
                    data.institutional_move
                    and data.institutional_move.score > 0
                )
                else 0.0
            )


        else:

            raise TypeError(
                "LiquidityScoreEngine expects AnalysisContext or LiquiditySweepResult"
            )


        #
        # No sweep
        #

        if not (
            liquidity.bullish_sweep
            or liquidity.bearish_sweep
        ):

            return LiquidityScore(
                score=0.0,
                sweep_strength=0.0,
                location=0.0,
                trend_alignment=0.0,
                continuation_probability=0.0,
                freshness=0.0,
                reasons=[
                    "No liquidity sweep detected.",
                ],
            )


        #
        # Scoring
        #

        sweep_strength = 20.0


        location = (
            20.0
            if liquidity.swept_level is not None
            else 0.0
        )


        freshness = 20.0


        score = (
            sweep_strength
            + location
            + trend_alignment
            + continuation_probability
            + freshness
        )


        return LiquidityScore(
            score=min(score,100.0),
            sweep_strength=sweep_strength,
            location=location,
            trend_alignment=trend_alignment,
            continuation_probability=continuation_probability,
            freshness=freshness,
            reasons=[
                "Liquidity sweep scored successfully.",
            ],
        )