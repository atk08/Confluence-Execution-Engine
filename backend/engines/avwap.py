"""
Institutional Anchored VWAP scoring engine.
"""

from backend.models.market import AnchoredVWAP


class AVWAPEngine:
    """
    Calculates an AVWAP alignment score.
    """

    @staticmethod
    def calculate_score(avwap: AnchoredVWAP) -> float:
        score = 0.0

        # Respect Count (0–30)
        score += min(avwap.respect_count * 5, 30)

        # Trend Strength (0–20)
        score += min(abs(avwap.slope) * 20, 20)

        # Institutional Confluence
        if avwap.aligned_with_poc:
            score += 20

        if avwap.aligned_with_hvn:
            score += 15

        if avwap.aligned_with_lvn:
            score += 15

        return min(score, 100.0)