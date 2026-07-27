"""
Trade Planner.

Builds a complete trade plan from all analysis engines.
"""

from backend.engines.confluence_engine import ConfluenceEngine
from backend.engines.execution_engine import ExecutionEngine
from backend.engines.risk_engine import RiskEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.trade_plan import TradePlan


class TradePlanner:
    """
    Creates a complete TradePlan.
    """

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> TradePlan:

        execution = ExecutionEngine.analyze(context)

        risk = RiskEngine.analyze(
            context,
            execution,
        )

        confluence = ConfluenceEngine.analyze(context)

        return TradePlan(
            direction=execution.direction,
            confidence=execution.confidence,
            confluence_score=confluence.score,
            approved=risk.approved,
            entry_price=risk.entry_price,
            stop_loss=risk.stop_loss,
            take_profit=risk.take_profit,
            risk_reward=risk.risk_reward,
            reasons=execution.reasons + risk.reasons,
            warnings=execution.warnings,
        )