"""
FastAPI Application.

Main API entry point for Confluence Execution Engine.
"""

from dotenv import load_dotenv

load_dotenv()


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from backend.providers.twelve_data import (
    TwelveDataProvider,
)

from backend.services.scanner_service import (
    ScannerService,
)



app = FastAPI(
    title="Confluence Execution Engine",
    version="1.0.0",
    description="Institutional market analysis engine",
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



provider = TwelveDataProvider()



@app.get("/")
def root():

    return {
        "status": "online",
        "service": "Confluence Execution Engine",
        "version": "1.0.0",
    }



@app.get("/health")
def health():

    return {
        "status": "healthy",
        "engine": "Confluence Execution Engine",
        "version": "1.0.0",
    }



@app.get("/scan/{symbol}")
def scan(
    symbol: str,
    interval: str = "5min",
    outputsize: int = 100,
):

    try:

        market_symbol = symbol.upper()


        if market_symbol == "BTC":
            market_symbol = "BTC/USD"

        elif market_symbol == "ETH":
            market_symbol = "ETH/USD"



        candles = provider.get_candles(
            symbol=market_symbol,
            interval=interval,
            outputsize=outputsize,
        )


        if not candles:

            raise HTTPException(
                status_code=404,
                detail="No candle data returned.",
            )


        result = ScannerService.scan(
            candles=candles,
            symbol=market_symbol,
            timeframe=interval,
        )


        trade_plan = result.trade_plan



        return {

            "symbol": result.symbol,

            "timeframe": result.timeframe,

            "price": result.current_price,

            "bias": result.market_bias,


            "analysis": {

                "score": result.confluence.score,

                "signal": result.signal.signal,

                "confidence": result.signal.confidence,

                "summary": result.summary,

            },


            "execution": {

                "direction": (
                    trade_plan.direction
                    if trade_plan
                    else "NONE"
                ),

                "entry": (
                    trade_plan.entry
                    if trade_plan
                    else None
                ),

                "stop_loss": (
                    trade_plan.stop_loss
                    if trade_plan
                    else None
                ),

                "take_profit": (
                    trade_plan.take_profit_1
                    if trade_plan
                    else None
                ),

                "risk_reward": (
                    trade_plan.risk_reward
                    if trade_plan
                    else None
                ),

            },


            "details": {

                "confluence": result.confluence,

                "institutional_move": (
                    result.institutional_move
                ),

            },


            "reasons": result.reasons,

        }



    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )