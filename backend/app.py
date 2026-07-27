from dataclasses import asdict

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel

from backend.models.candles import Candle

from backend.pipelines.analysis_pipeline import (
    AnalysisPipeline,
)

from backend.engines.final_analysis_engine import (
    FinalAnalysisEngine,
)

from backend.providers.twelve_data import (
    TwelveDataProvider,
)


app = FastAPI(
    title="Confluence Execution Engine",
    version="1.0.0",
)


class CandleRequest(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: float


@app.get("/")
def root():
    return {
        "status": "running",
        "engine": "Confluence Execution Engine",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "healthy": True,
        "engine": "ready",
    }


@app.post("/analyze")
def analyze(candles: list[CandleRequest]):

    candle_objects = [
        Candle(
            open=c.open,
            high=c.high,
            low=c.low,
            close=c.close,
            volume=c.volume,
        )
        for c in candles
    ]

    context = AnalysisPipeline.run(
        candle_objects
    )

    result = FinalAnalysisEngine.analyze(
        context
    )

    return asdict(result)


@app.get("/scan/{symbol:path}")
def scan(
    symbol: str,
    interval: str = Query("5min"),
    outputsize: int = Query(100),
):

    # Normalize symbol
    symbol = symbol.upper()

    # Force crypto format
    if symbol in [
        "BTC",
        "ETH",
        "SOL",
        "XRP",
    ]:
        symbol = f"{symbol}/USD"

    provider = TwelveDataProvider()

    try:
        candles = provider.get_candles(
            symbol=symbol,
            interval=interval,
            outputsize=outputsize,
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Market data error: {str(e)}",
        )

    if not candles:
        raise HTTPException(
            status_code=404,
            detail="No candles returned for symbol.",
        )

    context = AnalysisPipeline.run(
        candles
    )

    result = FinalAnalysisEngine.analyze(
        context,
        symbol=symbol,
        timeframe=interval,
    )

    return asdict(result)