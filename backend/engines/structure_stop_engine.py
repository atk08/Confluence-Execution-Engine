"""
Structure Stop Engine.

Determines a stop-loss based on market structure.
Version 1 uses swing highs/lows with an ATR fallback.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.engines.atr_engine import ATREngine
from backend.engines.swing_detector import SwingDetector
from backend.models.analysis_context import AnalysisContext
from backend.models.stop_result import StopResult
from backend.models.trade_direction import TradeDirection


class StructureStopEngine(AnalysisEngine):
    """
    Calculates a structure-based stop loss.
    """

    name = "Structure Stop"

    ATR_BUFFER = 0.5

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
        direction: TradeDirection,
    ) -> StopResult:

        candles = context.candles
        entry = candles[-1].close

        atr = ATREngine.analyze(context).value

        if atr <= 0:
            atr = max(entry * 0.01, 0.01)

        swings = SwingDetector.detect_swings(candles)

        #
        # BUY
        #

        if direction == TradeDirection.BUY:

            swing_lows = [
                swing
                for swing in swings
                if swing.kind == "LOW"
            ]

            if swing_lows:

                latest = swing_lows[-1]

                return StopResult(
                    stop_price=round(
                        latest.price - (atr * cls.ATR_BUFFER),
                        2,
                    ),
                    source="Swing Low",
                    reason="Latest confirmed swing low with ATR buffer.",
                )

            return StopResult(
                stop_price=round(entry - atr, 2),
                source="ATR",
                reason="No confirmed swing low.",
                fallback_used=True,
            )

        #
        # SELL
        #

        swing_highs = [
            swing
            for swing in swings
            if swing.kind == "HIGH"
        ]

        if swing_highs:

            latest = swing_highs[-1]

            return StopResult(
                stop_price=round(
                    latest.price + (atr * cls.ATR_BUFFER),
                    2,
                ),
                source="Swing High",
                reason="Latest confirmed swing high with ATR buffer.",
            )

        return StopResult(
            stop_price=round(entry + atr, 2),
            source="ATR",
            reason="No confirmed swing high.",
            fallback_used=True,
        )