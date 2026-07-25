# Confluence Execution Engine Architecture

## Vision

The Confluence Execution Engine is an institutional-grade market analysis engine.

Its purpose is not to predict the future.

Its purpose is to evaluate the current market state and determine the probability of a high-quality trading opportunity.

---

# Design Principles

Every engine has ONE responsibility.

Engines never duplicate logic.

Engines communicate through strongly typed models.

Every engine must be independently testable.

Every engine returns market state rather than raw events whenever possible.

---

# Execution Pipeline

Raw Market Data

↓

Normalization

↓

Structure Analysis

↓

Trend Analysis

↓

Institutional Analysis

↓

Market Context

↓

Confluence Scoring

↓

Human Explanation

↓

API Response

---

# Layer 1

Market Data

Responsibilities

- Data Provider
- Candle Validation
- Normalization

Output

List[Candle]

---

# Layer 2

Market Structure

Engines

- SwingDetector
- HigherHighAnalyzer
- HigherLowAnalyzer
- StructureEngine
- TrendEngine

Output

StructureResult

TrendResult

---

# Layer 3

Institutional Concepts

Engines

- Break Of Structure
- Change Of Character
- Liquidity Sweep
- Fair Value Gap
- Order Block
- Mitigation
- Premium / Discount

Each engine operates independently.

Each engine returns its own Result object.

---

# Layer 4

Volume Analysis

Engines

- Anchored VWAP
- Volume Profile

Output

InstitutionalAnalysis

---

# Layer 5

Market Context

Purpose

Merge every engine into one coherent picture of the market.

Example

Trend

Bullish

Liquidity

Buy-side sweep

FVG

Fresh

Order Block

Untouched

Volume

Above POC

AVWAP

Above

---

# Layer 6

Confluence Engine

Purpose

Assign probability score.

Output

0

↓

100

---

# Layer 7

Explanation Engine

Purpose

Explain WHY the score exists.

Example

BTC is scoring 91 because

• Strong bullish trend

• Fresh liquidity sweep

• Bullish CHoCH

• Fresh Fair Value Gap

• Above Anchored VWAP

• Above Point Of Control

Risk

Moderate

---

# Engine Rules

Every engine

Must

✔ Be deterministic

✔ Have unit tests

✔ Return typed models

✔ Never perform API calls

✔ Never print

✔ Never mutate data

✔ Never know UI exists

---

# Dependency Rules

Allowed

Trend

↓

Structure

Liquidity

↓

Structure

FVG

↓

Candles

Market Context

↓

Everything

Confluence

↓

Everything

Forbidden

Structure

↓

Trend

Trend

↓

Confluence

Liquidity

↓

Order Block

Order Block

↓

UI

---

# Scoring Philosophy

Scores are based on confluence.

No single indicator can produce 100.

Higher scores require multiple institutional confirmations.

---

# Future Roadmap

Current

✓ Structure

✓ Trend

✓ BOS

✓ CHoCH

✓ Liquidity

In Progress

• Fair Value Gap

Upcoming

• Order Block

• Mitigation

• Premium Discount

• Market Context

• Confluence Engine

• Explanation Engine

Long Term

• Multi-Timeframe Analysis

• Forex

• Stocks

• ETFs

• AI Weight Optimization

• Strategy Builder

• Alerts

• Portfolio Analysis