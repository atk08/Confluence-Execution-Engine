"""
Market data provider interfaces.
"""

from abc import ABC, abstractmethod

from backend.models.candles import Candle


class MarketDataProvider(ABC):
    """
    Base interface for market data providers.
    """

    @abstractmethod
    def get_candles(
        self,
        symbol: str,
        timeframe: str,
        limit: int,
    ) -> list[Candle]:
        """
        Return a list of candles.
        """
        raise NotImplementedError