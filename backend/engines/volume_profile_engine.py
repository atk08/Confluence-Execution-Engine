"""
Institutional Volume Profile Engine.

Builds a basic institutional Volume Profile from candle data.
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

        total_volume = sum(c.volume for c in candles)

        if total_volume == 0:
            return VolumeProfileResult(
                score=0.0,
                bullish=False,
                bearish=False,
                poc=None,
                value_area_high=None,
                value_area_low=None,
            )

        # --------------------------------------------------
        # Find Point Of Control (highest volume candle)
        # --------------------------------------------------

        poc_candle = max(
            candles,
            key=lambda candle: candle.volume,
        )

        poc = poc_candle.close

        # --------------------------------------------------
        # Approximate Value Area
        # --------------------------------------------------

        highs = [c.high for c in candles]
        lows = [c.low for c in candles]

        session_high = max(highs)
        session_low = min(lows)

        session_range = session_high - session_low

        value_area_high = session_low + session_range * 0.85
        value_area_low = session_low + session_range * 0.15

        # --------------------------------------------------
        # Market Bias
        # --------------------------------------------------

        last_close = candles[-1].close

        bullish = last_close > poc
        bearish = last_close < poc

        # --------------------------------------------------
        # Institutional Score
        # --------------------------------------------------

        score = 0.0

        if bullish or bearish:
            score += 40

        if value_area_low <= last_close <= value_area_high:
            score += 30

        if abs(last_close - poc) / poc < 0.01:
            score += 30

        return VolumeProfileResult(
            score=min(score, 100.0),
            bullish=bullish,
            bearish=bearish,
            poc=poc,
            value_area_high=value_area_high,
            value_area_low=value_area_low,
        )