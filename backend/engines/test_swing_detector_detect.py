from backend.engines.swing_detector import SwingDetector
from backend.models.candles import Candle


def test_detect_swings():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 105, 98, 104, 1000),
        Candle(104, 102, 97, 101, 1000),
        Candle(101, 106, 100, 105, 1000),
        Candle(105, 103, 99, 102, 1000),
    ]

    swings = SwingDetector.detect_swings(candles)

    assert len(swings) == 3

    assert swings[0].kind == "HIGH"
    assert swings[0].price == 105

    assert swings[1].kind == "LOW"
    assert swings[1].price == 97

    assert swings[2].kind == "HIGH"
    assert swings[2].price == 106