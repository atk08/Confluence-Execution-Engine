import pytest

from backend.data.market_data import MarketDataProvider


def test_market_data_provider_is_abstract():
    with pytest.raises(TypeError):
        MarketDataProvider()