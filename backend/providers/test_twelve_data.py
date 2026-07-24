import os

import pytest

from backend.providers.twelve_data import TwelveDataProvider


@pytest.mark.skipif(
    not os.getenv("TWELVE_DATA_API_KEY"),
    reason="TWELVE_DATA_API_KEY not configured",
)
def test_download_candles():

    provider = TwelveDataProvider()

    candles = provider.get_candles(
        symbol="BTC/USD",
        interval="1h",
        outputsize=10,
    )

    assert len(candles) == 10