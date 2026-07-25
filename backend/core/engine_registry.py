"""
Simple registry for analysis engines.
"""

from backend.core.analysis_engine import AnalysisEngine


class EngineRegistry:
    """
    Stores registered analysis engines.
    """

    _engines: dict[str, type[AnalysisEngine]] = {}

    @classmethod
    def register(cls, engine: type[AnalysisEngine]) -> None:
        cls._engines[engine.name] = engine

    @classmethod
    def get(cls, name: str) -> type[AnalysisEngine]:
        return cls._engines[name]

    @classmethod
    def all(cls) -> dict[str, type[AnalysisEngine]]:
        return dict(cls._engines)