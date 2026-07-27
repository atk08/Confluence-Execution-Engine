"""
Execution Timing Engine.

Determines whether current price action is suitable
for entering a trade.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.execution_result import ExecutionResult
from backend.models.execution_timing_result import ExecutionTimingResult
from backend.models.trade_direction import TradeDirection


class ExecutionTimingEngine(AnalysisEngine):
    """
    Simple execution timing engine.

    Version 1 confirms that price is moving
    in the intended direction.
    """

    name = "Execution Timing"

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
        execution: ExecutionResult,
    ) -> ExecutionTimingResult:

        candles = context.candles

        if len(candles) < 2:
            return ExecutionTimingResult(
                ready=False,
                timing_score=0.0,
                reasons=["Not enough candles."],
            )

        previous = candles[-2]
        current = candles[-1]

        #
        # BUY
        #

        if execution.direction == TradeDirection.BUY:

            if current.close > previous.close:
                return ExecutionTimingResult(
                    ready=True,
                    timing_score=100.0,
                    reasons=[
                        "Bullish confirmation candle detected."
                    ],
                )

            return ExecutionTimingResult(
                ready=False,
                timing_score=0.0,
                reasons=[
                    "No bullish confirmation candle."
                ],
            )

        #
        # SELL
        #

        if current.close < previous.close:
            return ExecutionTimingResult(
                ready=True,
                timing_score=100.0,
                reasons=[
                    "Bearish confirmation candle detected."
                ],
            )

        return ExecutionTimingResult(
            ready=False,
            timing_score=0.0,
            reasons=[
                "No bearish confirmation candle."
            ],
        )