# Mathematical Specification

Version: 1.0

Status: Draft

---

# Purpose

This document defines the mathematical rules governing every calculation performed by the Confluence Engine.

The objective is to ensure that every score produced by the engine is:

- Objective
- Deterministic
- Explainable
- Testable
- Version Controlled

No score may be generated from subjective interpretation.

Every calculation must be reproducible.

---

# Mathematical Philosophy

The engine does not predict price.

The engine measures evidence.

Evidence is evaluated independently.

Evidence is combined into Confluence Zones.

Confluence Zones are evaluated within Market Context.

The Institutional Confidence Engine converts measurable evidence into a final Institutional Confidence Score.

---

# Mathematical Pipeline

Raw Market Data

↓

Evidence Detection

↓

Evidence Measurement

↓

Evidence Quality

↓

Evidence Integrity

↓

Evidence Weighting

↓

Confluence Strength

↓

Market Context Adjustment

↓

Institutional Confidence Score
---

# MATH-001

## Point of Control (POC) Quality

### Purpose

The POC Quality formula measures the significance of a Point of Control within a defined auction period.

The objective is to estimate how important that POC is as an institutional reference level.

The formula evaluates the quality of the auction itself.

It does not evaluate future price direction.

---

## Inputs

The following variables contribute to POC Quality:

- Volume Concentration
- Time at Price
- Auction Acceptance
- Historical Reactions
- Distance from Current Price
- Session Importance
- Recency

Each variable is independently normalized to a score between 0 and 100.

---

## Output

POC Quality

Range:

0–100

Interpretation:

0–40

Weak

41–70

Moderate

71–85

Strong

86–100

Institutional
---

# MATH-002

## Point of Control (POC) Integrity

### Purpose

POC Integrity measures how "untouched" a Point of Control remains.

Unlike POC Quality, which measures the importance of the auction, Integrity measures the probability that the level will still produce a meaningful institutional reaction.

Integrity decreases as price repeatedly trades through the level.

POC Integrity does not measure trend direction.

It measures preservation of institutional interest.

---

## Philosophy

A Point of Control represents an area where significant business was conducted.

The first return to a high-quality auction often carries more informational value than subsequent visits.

Every revisit potentially reduces the remaining imbalance.

Integrity therefore measures how much of that original auction remains untested.

---

## Inputs

The following variables contribute to POC Integrity:

- Number of Revisits
- Penetration Depth
- Time Spent During Revisits
- Acceptance After Revisit
- Clean Rejections
- Time Since Last Touch

Each variable is normalized between 0 and 100.

---

## Output

POC Integrity

Range:

0–100

Interpretation:

90–100 = Untouched

75–89 = Excellent

60–74 = Good

40–59 = Weakening

0–39 = Degraded
---

# MATH-003

## High Volume Node (HVN) Quality

### Purpose

HVN Quality measures the significance of a High Volume Node as an area of institutional acceptance.

The formula evaluates whether the node represents meaningful value or merely accumulated volume.

---

## Inputs

- Volume Density
- Node Width
- Acceptance Duration
- Relationship to POC
- Historical Reactions
- Session Importance

---

## Output

HVN Quality

Range:

0–100
---

# Fundamental Scoring Principle

The Confluence Engine never scores indicators.

The engine evaluates evidence.

Each Evidence Object contains two independent measurements.

## Quality

Quality measures the significance of the evidence within the current market.

Quality is calculated entirely from current market data.

Quality answers:

"How strong is this evidence today?"

---

## Reliability

Reliability measures the historical predictive performance of this type of evidence.

Reliability is calculated from the Research Framework.

Reliability answers:

"How much historical trust should we place in this evidence?"

---

Quality and Reliability must never be confused.

Quality describes the present.

Reliability describes the past.

Together they form the basis for institutional confidence.