"""
Confluence Score Engine.
"""


class ConfluenceScore:
    """
    Combines multiple analysis scores into a single
    institutional confluence score.
    """

    WEIGHTS = {
        "trend": 20,
        "avwap": 15,
        "volume_profile": 25,
        "momentum": 15,
        "structure": 15,
        "volatility": 10,
    }

    @classmethod
    def calculate(cls, scores: dict) -> dict:
        """
        Calculate the weighted confluence score.

        Parameters
        ----------
        scores
            Dictionary containing normalized values
            between 0.0 and 1.0.
        """

        breakdown = {}

        total = 0

        for category, weight in cls.WEIGHTS.items():

            value = scores.get(category, 0)

            weighted = round(value * weight, 2)

            breakdown[category] = weighted

            total += weighted

        total = round(total, 2)

        if total >= 85:
            recommendation = "Strong Bullish"
        elif total >= 70:
            recommendation = "Bullish"
        elif total >= 50:
            recommendation = "Neutral"
        elif total >= 30:
            recommendation = "Bearish"
        else:
            recommendation = "Strong Bearish"

        return {
            "score": total,
            "breakdown": breakdown,
            "recommendation": recommendation,
        }