"""
Liquidity Score Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.liquidity_score import LiquidityScore
from backend.models.liquidity_sweep_result import LiquiditySweepResult


class LiquidityScoreEngine(AnalysisEngine):
    """
    Scores a liquidity sweep from 0–100.
    """

    name = "Liquidity Score"

    @classmethod
    def analyze(
        cls,
        liquidity: LiquiditySweepResult,
    ) -> LiquidityScore:

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

        sweep_strength = 20.0
        location = 20.0
        trend_alignment = 20.0
        continuation_probability = 20.0
        freshness = 20.0

        score = (
            sweep_strength
            + location
            + trend_alignment
            + continuation_probability
            + freshness
        )

        return LiquidityScore(
            score=score,
            sweep_strength=sweep_strength,
            location=location,
            trend_alignment=trend_alignment,
            continuation_probability=continuation_probability,
            freshness=freshness,
            reasons=[
                "Liquidity sweep scored successfully.",
            ],
        )