from backend.core.analysis_engine import AnalysisEngine
from backend.core.engine_registry import EngineRegistry


class DummyEngine(AnalysisEngine):
    name = "Dummy"

    @classmethod
    def analyze(cls, candles):
        return None


def test_register_engine():

    EngineRegistry.register(DummyEngine)

    engine = EngineRegistry.get("Dummy")

    assert engine is DummyEngine