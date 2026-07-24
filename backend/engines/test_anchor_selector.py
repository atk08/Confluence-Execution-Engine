from backend.engines.anchor_selector import AnchorSelector
from backend.models.candles import Candle


def test_select_high_anchor():
    swings = [
        Candle(open=95, high=100, low=90, close=95, volume=1000),
        Candle(open=100, high=110, low=92, close=100, volume=1200),
        Candle(open=97, high=105, low=91, close=97, volume=900),
    ]

    anchor = AnchorSelector.select_high_anchor(swings)

    assert anchor.high == 110


def test_select_low_anchor():
    swings = [
        Candle(open=95, high=100, low=90, close=95, volume=1000),
        Candle(open=96, high=105, low=85, close=96, volume=1300),
        Candle(open=94, high=103, low=88, close=94, volume=950),
    ]

    anchor = AnchorSelector.select_low_anchor(swings)

    assert anchor.low == 85