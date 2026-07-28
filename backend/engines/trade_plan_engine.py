"""
Trade Plan Engine.

Creates execution levels:
- Entry
- Stop Loss
- Take Profit
- Risk Reward

Uses:
- Market direction
- Swing structure
- Liquidity levels
- ATR-ready architecture
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_context import AnalysisContext

from backend.models.trade_plan_result import (
    TradePlanResult,
)


class TradePlanEngine(AnalysisEngine):

    name = "Trade Plan Engine"


    RISK_REWARD = 2.0


    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
        direction: str,
    ) -> TradePlanResult:


        if not context.candles:

            return TradePlanResult(
                direction="NONE",
                entry=0.0,
                stop_loss=0.0,
                take_profit_1=0.0,
                risk_reward=0.0,
                reasons=[
                    "No candles available."
                ],
            )


        current_price = (
            context.candles[-1].close
        )


        reasons = []


        #
        # LONG SETUP
        #

        if direction == "BULLISH":


            entry = current_price


            if (
                context.structure.latest_swing_low
                is not None
            ):

                stop_loss = (
                    context.structure
                    .latest_swing_low
                    .price
                )

                reasons.append(
                    "Stop loss placed below latest swing low."
                )

            else:

                stop_loss = (
                    entry * 0.99
                )

                reasons.append(
                    "Fallback 1% stop loss used."
                )


            risk = entry - stop_loss


            if risk <= 0:

                stop_loss = entry * 0.99

                risk = entry - stop_loss


            take_profit = (
                entry
                +
                (
                    risk * cls.RISK_REWARD
                )
            )


            return TradePlanResult(
                direction="LONG",
                entry=entry,
                stop_loss=stop_loss,
                take_profit_1=take_profit,
                risk_reward=cls.RISK_REWARD,
                reasons=[
                    *reasons,
                    "Bullish trade plan created.",
                ],
            )


        #
        # SHORT SETUP
        #

        if direction == "BEARISH":


            entry = current_price


            if (
                context.structure.latest_swing_high
                is not None
            ):

                stop_loss = (
                    context.structure
                    .latest_swing_high
                    .price
                )

                reasons.append(
                    "Stop loss placed above latest swing high."
                )

            else:

                stop_loss = (
                    entry * 1.01
                )

                reasons.append(
                    "Fallback 1% stop loss used."
                )


            risk = stop_loss - entry


            if risk <= 0:

                stop_loss = entry * 1.01

                risk = stop_loss - entry


            take_profit = (
                entry
                -
                (
                    risk * cls.RISK_REWARD
                )
            )


            return TradePlanResult(
                direction="SHORT",
                entry=entry,
                stop_loss=stop_loss,
                take_profit_1=take_profit,
                risk_reward=cls.RISK_REWARD,
                reasons=[
                    *reasons,
                    "Bearish trade plan created.",
                ],
            )


        #
        # NO VALID DIRECTION
        #

        return TradePlanResult(
            direction="NONE",
            entry=current_price,
            stop_loss=current_price,
            take_profit_1=current_price,
            risk_reward=0.0,
            reasons=[
                "No directional bias. No trade plan created."
            ],
        )