from backend.engines.confluence_score import ConfluenceScore


def test_perfect_score():

    result = ConfluenceScore.calculate(
        {
            "trend": 1,
            "avwap": 1,
            "volume_profile": 1,
            "momentum": 1,
            "structure": 1,
            "volatility": 1,
        }
    )

    assert result["score"] == 100
    assert result["recommendation"] == "Strong Bullish"


def test_zero_score():

    result = ConfluenceScore.calculate({})

    assert result["score"] == 0
    assert result["recommendation"] == "Strong Bearish"


def test_half_score():

    result = ConfluenceScore.calculate(
        {
            "trend": 0.5,
            "avwap": 0.5,
            "volume_profile": 0.5,
            "momentum": 0.5,
            "structure": 0.5,
            "volatility": 0.5,
        }
    )

    assert result["score"] == 50
    assert result["recommendation"] == "Neutral"