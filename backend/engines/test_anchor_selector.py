from backend.engines.anchor_selector import AnchorSelector
from backend.engines.swing_detector import Candle


def test_select_high_anchor():
    swings = [
        Candle(100, 90, 95),
        Candle(110, 92, 100),
        Candle(105, 91, 97),
    ]

    anchor = AnchorSelector.select_high_anchor(swings)

    assert anchor.high == 110


def test_select_low_anchor():
    swings = [
        Candle(100, 90, 95),
        Candle(105, 85, 96),
        Candle(103, 88, 94),
    ]

    anchor = AnchorSelector.select_low_anchor(swings)

    assert anchor.low == 85