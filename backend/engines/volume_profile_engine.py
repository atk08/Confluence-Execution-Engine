"""
Institutional Volume Profile Engine.

Handles both real volume feeds and zero-volume crypto feeds.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.volume_profile_result import VolumeProfileResult


class VolumeProfileEngine(AnalysisEngine):
    """
    Performs Volume Profile analysis.
    """

    name = "Volume Profile"

    @classmethod
    def analyze(cls, candles):

        if not candles:
            return VolumeProfileResult(
                score=0.0,
                bullish=False,
                bearish=False,
                poc=None,
                value_area_high=None,
                value_area_low=None,
            )

        closes = [
            candle.close
            for candle in candles
        ]

        highs = [
            candle.high
            for candle in candles
        ]

        lows = [
            candle.low
            for candle in candles
        ]

        total_volume = sum(
            candle.volume
            for candle in candles
        )

        # -----------------------------------
        # Real Volume Mode
        # -----------------------------------

        if total_volume > 0:

            poc_candle = max(
                candles,
                key=lambda candle: candle.volume,
            )

            poc = poc_candle.close

        # -----------------------------------
        # Crypto Fallback Mode
        # -----------------------------------

        else:

            price_frequency = {}

            for price in closes:

                rounded = round(price, 2)

                price_frequency[rounded] = (
                    price_frequency.get(
                        rounded,
                        0
                    )
                    + 1
                )

            poc = max(
                price_frequency,
                key=price_frequency.get,
            )

        session_high = max(highs)

        session_low = min(lows)

        session_range = (
            session_high - session_low
        )

        value_area_high = (
            session_low
            + session_range * 0.85
        )

        value_area_low = (
            session_low
            + session_range * 0.15
        )

        last_close = candles[-1].close

        bullish = last_close > poc
        bearish = last_close < poc

        score = 0.0

        # Price acceptance
        if bullish or bearish:
            score += 40

        # Inside value area
        if (
            value_area_low
            <= last_close
            <= value_area_high
        ):
            score += 30

        # Near POC
        if poc != 0:

            distance = abs(
                last_close - poc
            ) / poc

            if distance < 0.01:
                score += 30

        return VolumeProfileResult(
            score=min(score, 100.0),
            bullish=bullish,
            bearish=bearish,
            poc=poc,
            value_area_high=value_area_high,
            value_area_low=value_area_low,
        )