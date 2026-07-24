from backend.engines.avwap_calculator import AVWAPCalculator
from backend.models.candles import Candle


def test_avwap_calculation():
    candles = [
        Candle(open=100, high=110, low=90, close=100, volume=1000),
        Candle(open=100, high=120, low=100, close=110, volume=2000),
    ]

    avwap = AVWAPCalculator.calculate(candles)

    expected = (
        (((110 + 90 + 100) / 3) * 1000) +
        (((120 + 100 + 110) / 3) * 2000)
    ) / 3000

    assert round(avwap, 6) == round(expected, 6)


def test_empty_list_raises():
    import pytest

    with pytest.raises(ValueError):
        AVWAPCalculator.calculate([])