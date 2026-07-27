"""
Order Block Score Engine.

Calculates a quality score for an Order Block.
Version 1 provides a simple weighted scoring model.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.order_block_result import OrderBlockResult
from backend.models.order_block_score import OrderBlockScore


class OrderBlockScoreEngine(AnalysisEngine):
    """
    Scores an order block from 0 to 100.
    """

    name = "Order Block Score"

    @classmethod
    def analyze(
        cls,
        order_block: OrderBlockResult,
    ) -> OrderBlockScore:

        if not (
            order_block.bullish_block
            or order_block.bearish_block
        ):
            return OrderBlockScore(
                score=0.0,
                freshness=0.0,
                displacement=0.0,
                volume=0.0,
                trend_alignment=0.0,
                proximity=0.0,
                reasons=[
                    "No order block detected.",
                ],
            )

        freshness = 20.0
        displacement = 20.0
        volume = 20.0
        trend_alignment = 20.0
        proximity = 20.0

        if order_block.mitigated:
            freshness = 10.0

        if order_block.touched:
            proximity = 15.0

        if order_block.broken:
            trend_alignment = 10.0

        score = (
            freshness
            + displacement
            + volume
            + trend_alignment
            + proximity
        )

        return OrderBlockScore(
            score=score,
            freshness=freshness,
            displacement=displacement,
            volume=volume,
            trend_alignment=trend_alignment,
            proximity=proximity,
            reasons=[
                "Order block scored successfully.",
            ],
        )