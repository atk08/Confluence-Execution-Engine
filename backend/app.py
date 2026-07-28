"""
FastAPI Application.

Main API entry point for Confluence Execution Engine.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.providers.twelve_data import TwelveDataProvider
from backend.pipelines.analysis_pipeline import AnalysisPipeline
from backend.engines.final_analysis_engine import FinalAnalysisEngine


app = FastAPI(
    title="Confluence Execution Engine",
    version="1.0.0",
    description="Institutional market analysis engine",
)


#
# CORS
#

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#
# Market Data Provider
#

provider = TwelveDataProvider()



@app.get("/")
def root():

    return {
        "status": "online",
        "service": "Confluence Execution Engine",
    }



@app.get("/scan/{symbol}")
def scan(
    symbol: str,
    interval: str = "5min",
    outputsize: int = 100,
):

    try:

        #
        # Normalize symbols
        #

        market_symbol = symbol.upper()


        if market_symbol == "BTC":
            market_symbol = "BTC/USD"

        elif market_symbol == "ETH":
            market_symbol = "ETH/USD"



        #
        # Get candles
        #

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



        #
        # Run analysis pipeline
        #

        context = AnalysisPipeline.run(
            candles
        )



        #
        # Final analysis
        #

        result = FinalAnalysisEngine.analyze(
            context=context,
            symbol=market_symbol,
            timeframe=interval,
        )



        #
        # Return response
        #

        return {

            "symbol": result.symbol,

            "timeframe": result.timeframe,

            "current_price": result.current_price,

            "market_bias": result.market_bias,

            "confluence": result.confluence,

            "signal": result.signal,

            "institutional_move": result.institutional_move,

            "trade_plan": result.trade_plan,

            "summary": result.summary,

            "reasons": result.reasons,

        }



    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )