"""
Tests for AnalysisResultEngine.
"""

from backend.engines.analysis_result_engine import AnalysisResultEngine
from backend.models.confluence_score_v2 import ConfluenceScoreV2
from backend.models.trade_signal import Signal, TradeSignal


def test_analysis_result():

    confluence = ConfluenceScoreV2(
        score=85.0,
        market_structure=25.0,
        volume_profile=18.0,
        avwap=17.0,
        order_block=13.0,
        fair_value_gap=7.0,
        liquidity=5.0,
        reasons=[],
    )

    signal = TradeSignal(
        signal=Signal.BUY,
        confidence=85.0,
        confluence_score=85.0,
        reasons=[],
    )

    result = AnalysisResultEngine.analyze(
        symbol="BTCUSDT",
        timeframe="1h",
        confluence=confluence,
        signal=signal,
    )

    assert result.symbol == "BTCUSDT"
    assert result.timeframe == "1h"
    assert result.signal.signal == Signal.BUY
    assert result.confluence.score == 85.0