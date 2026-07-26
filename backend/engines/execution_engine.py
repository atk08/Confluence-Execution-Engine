"""
Execution Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.engines.confluence_engine import ConfluenceEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.execution_confidence import ExecutionConfidence
from backend.models.execution_result import ExecutionResult
from backend.models.trade_direction import TradeDirection


class ExecutionEngine(AnalysisEngine):
    """
    Produces a complete trade recommendation from the
    current AnalysisContext.
    """

    name = "Execution"

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> ExecutionResult:

        confluence = ConfluenceEngine.analyze(context)

        score = confluence.score

        reasons: list[str] = []
        warnings: list[str] = []

        #
        # Confidence
        #

        if score >= 80:
            confidence = ExecutionConfidence.VERY_HIGH
        elif score >= 65:
            confidence = ExecutionConfidence.HIGH
        elif score >= 50:
            confidence = ExecutionConfidence.MEDIUM
        else:
            confidence = ExecutionConfidence.LOW

        #
        # Direction
        #

        if confluence.bullish:
            direction = TradeDirection.BUY
        elif confluence.bearish:
            direction = TradeDirection.SELL
        else:
            direction = TradeDirection.NEUTRAL

        #
        # Reasons
        #

        if context.trend.score > 0:
            reasons.append("Trend is aligned.")

        if context.structure.score > 0:
            reasons.append("Market structure is supportive.")

        if (
            context.institutional_move
            and context.institutional_move.bullish_move
        ):
            reasons.append("Bullish institutional move confirmed.")

        if (
            context.institutional_move
            and context.institutional_move.bearish_move
        ):
            reasons.append("Bearish institutional move confirmed.")

        #
        # Warnings
        #

        if score < 70:
            warnings.append(
                "Overall confluence is below the execution threshold."
            )

        if not reasons:
            warnings.append(
                "No strong technical confirmations detected."
            )

        should_trade = score >= 70

        return ExecutionResult(
            trade_score=score,
            direction=direction,
            confidence=confidence,
            should_trade=should_trade,
            entry_price=None,
            stop_loss=None,
            take_profit=None,
            risk_reward=None,
            reasons=reasons,
            warnings=warnings,
        )