"""
Risk Engine.

Calculates a trade risk profile using the execution result.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.engines.atr_engine import ATREngine
from backend.engines.structure_stop_engine import StructureStopEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.execution_result import ExecutionResult
from backend.models.risk_result import RiskResult


class RiskEngine(AnalysisEngine):
    """
    Produces a structure-aware risk assessment.
    """

    name = "Risk"

    RISK_REWARD_THRESHOLD = 2.0

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
        execution: ExecutionResult,
    ) -> RiskResult:

        if not context.candles:
            return RiskResult(
                entry_price=None,
                stop_loss=None,
                take_profit=None,
                risk=None,
                reward=None,
                risk_reward=None,
                approved=False,
                reasons=["No market data available."],
            )

        entry = context.candles[-1].close

        atr = ATREngine.analyze(context).value

        if atr <= 0:
            atr = max(entry * 0.01, 0.01)

        #
        # Structure-based stop loss
        #

        stop_result = StructureStopEngine.analyze(
            context,
            execution.direction,
        )

        stop = round(stop_result.stop_price, 2)

        #
        # Risk is based on the structure stop.
        #

        risk = round(abs(entry - stop), 2)

        #
        # Maintain a 2:1 reward:risk ratio.
        #

        if execution.direction == execution.direction.BUY:
            target = round(entry + (risk * 2), 2)
        else:
            target = round(entry - (risk * 2), 2)

        reward = round(abs(target - entry), 2)

        risk_reward = (
            round(reward / risk, 2)
            if risk > 0
            else None
        )

        approved = (
            risk_reward is not None
            and risk_reward >= cls.RISK_REWARD_THRESHOLD
        )

        reasons = []

        if approved:
            reasons.append(
                "Risk/reward meets minimum threshold."
            )
        else:
            reasons.append(
                "Risk/reward below minimum threshold."
            )

        reasons.append(stop_result.reason)
        reasons.append(f"Stop source: {stop_result.source}")
        reasons.append(f"ATR used: {atr:.2f}")

        return RiskResult(
            entry_price=entry,
            stop_loss=stop,
            take_profit=target,
            risk=risk,
            reward=reward,
            risk_reward=risk_reward,
            approved=approved,
            reasons=reasons,
        )