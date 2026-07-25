"""
Base class for all analysis engines.
"""

from abc import ABC, abstractmethod

from backend.models.candles import Candle


class AnalysisEngine(ABC):
    """
    Base class for every analysis engine.
    """

    name = "BaseEngine"

    @classmethod
    @abstractmethod
    def analyze(cls, candles: list[Candle]):
        """
        Analyze market data and return a result model.
        """
        raise NotImplementedError