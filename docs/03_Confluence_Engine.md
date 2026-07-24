# Confluence Engine Specification

**Version:** 1.0  
**Status:** Draft  
**Last Updated:** July 2026

---

# Purpose

The Confluence Engine is the core intelligence behind Confluence Scanner AI.

Its purpose is not to predict the future.

Its purpose is to identify **high-probability institutional trading locations** by measuring the confluence of independent auction-based market factors.

Every output produced by the engine must be:

- Objective
- Explainable
- Repeatable
- Measurable

The engine never scores an asset.

It scores **locations**.

These locations are called **Confluence Zones**.

---

# Mission Statement

Help traders understand **where institutions are most likely to transact and why.**

The engine should simplify market analysis by combining multiple institutional concepts into a single transparent confidence rating.

---

# Core Philosophy

Markets operate as auctions.

Institutions leave measurable footprints through:

- Volume
- Acceptance
- Rejection
- Imbalance
- Average traded price

The Confluence Engine identifies and scores these footprints.
---

# Confluence Zones

## Definition

A Confluence Zone is a price area where multiple independent institutional factors overlap within a defined price tolerance.

The engine scores the zone rather than the individual indicators.

A Confluence Zone is the smallest tradable unit within the Confluence Engine.

---

## Objective

Instead of asking:

"Is there a Fair Value Gap?"

The engine asks:

"How many institutional reasons exist to transact at this location?"

---

## Institutional Factors

A Confluence Zone may contain one or more of the following:

- Point of Control (POC)
- High Volume Node (HVN)
- Low Volume Node (LVN)
- Value Area High (VAH)
- Value Area Low (VAL)
- Anchored VWAP
- Fair Value Gap (FVG)
- Relative Volume Expansion
- Future: Order Flow
- Future: Options Flow
- Future: Open Interest

---

## Zone Creation

The engine begins by plotting every institutional level.

Nearby levels are then clustered together.

Example:

POC

118250

HVN

118265

Bullish FVG

118270

Anchored VWAP

118255

↓

These become:

Confluence Zone

118250 – 118270

The engine scores the zone rather than the four individual levels.

---

## Why Zones Matter

Institutions rarely transact at one exact price.

They transact across areas.

The engine therefore evaluates price regions instead of individual ticks.

This creates more realistic execution levels while reducing noise.
---

# Confluence Pipeline

Every asset analyzed by the Confluence Engine follows the same deterministic pipeline.

No market is treated differently.

Every score is generated using the same sequence of independent analysis engines.

```
Market Data
      │
      ▼
Market Environment Engine
      │
      ▼
Volume Profile Engine
      │
      ▼
Anchored VWAP Engine
      │
      ▼
Fair Value Gap Engine
      │
      ▼
Volume Behaviour Engine
      │
      ▼
Confluence Zone Engine
      │
      ▼
Institutional Confidence Engine
      │
      ▼
Auction Story Engine
      │
      ▼
Trade Plan Engine
```

Each engine performs one responsibility only.

No engine should contain logic belonging to another engine.

This separation makes the platform easier to test, improve, and maintain.

---

# Engine Responsibilities

## 1. Market Environment Engine

Purpose:

Determine what type of market currently exists.

Possible classifications:

- Trending Bullish
- Trending Bearish
- Ranging
- Breakout
- Compression
- Expansion
- High Volatility
- Low Volatility

The market environment influences how every subsequent engine is weighted.

---

## 2. Volume Profile Engine

Purpose:

Identify where the market has accepted and rejected value.

Outputs:

- Point of Control (POC)
- Value Area High (VAH)
- Value Area Low (VAL)
- High Volume Nodes (HVNs)
- Low Volume Nodes (LVNs)

The Volume Profile Engine produces institutional price levels only.

It does not generate trade signals.

---

## 3. Anchored VWAP Engine

Purpose:

Determine the institutional average traded price.

Outputs:

- Anchored VWAP
- VWAP Direction
- Distance from Price
- Confluence with Volume Profile

---

## 4. Fair Value Gap Engine

Purpose:

Identify auction imbalances.

Outputs:

- Bullish FVGs
- Bearish FVGs
- Gap Freshness
- Gap Mitigation
- Gap Quality

---

## 5. Volume Behaviour Engine

Purpose:

Measure participation.

Outputs:

- Relative Volume
- Volume Expansion
- Volume Contraction
- Buying Pressure
- Selling Pressure

---

## 6. Confluence Zone Engine

Purpose:

Merge nearby institutional levels into unified trading zones.

Outputs:

- Zone Width
- Zone Strength
- Zone Type
- Supporting Evidence

---

## 7. Institutional Confidence Engine

Purpose:

Calculate the Institutional Confidence Score (ICS).

Outputs:

- Raw Evidence
- Weighted Evidence
- Institutional Confidence Score
- Confidence Rating

---

## 8. Auction Story Engine

Purpose:

Translate technical evidence into a plain-language explanation.

Outputs:

- Institutional Narrative
- Expected Behaviour
- Market Context

---

## 9. Trade Plan Engine

Purpose:

Generate a complete execution plan.

Outputs:

- Entry Zone
- Invalidation Level
- Target Levels
- Risk/Reward
- Trade Quality
---

# Engine Design Principles

The Confluence Engine is composed of independent analysis engines.

Each engine has one responsibility.

Each engine receives an input, performs one analysis, and returns a standardized output.

No engine is allowed to calculate another engine's responsibility.

This separation ensures the platform remains modular, testable, and maintainable.

---

## Standard Engine Contract

Every engine must follow the same structure.

### Input

Raw market data required by the engine.

### Processing

Engine-specific calculations.

### Output

A standardized result object.

Each engine returns:

- Engine Name
- Quality Score (0–100)
- Confidence
- Supporting Evidence
- Price Levels
- Metadata

The output is consumed by the next stage of the pipeline.

---

# Engine Independence

Example

Volume Profile Engine

Input

Market data

Output

POC

HVNs

LVNs

VAH

VAL

Quality Score

---

Anchored VWAP Engine

Input

Market data

Output

Anchored VWAP

Slope

Distance

Quality Score

---

Fair Value Gap Engine

Input

Candlestick data

Output

Bullish FVGs

Bearish FVGs

Gap Quality

Freshness

---

The Confluence Zone Engine combines outputs.

It never calculates POCs.

It never detects Fair Value Gaps.

It never calculates VWAP.

Its responsibility is clustering.

---

# Benefits

This architecture allows:

- Independent testing
- Independent optimization
- Easier debugging
- Future AI improvements
- Easier parallel processing
- Cleaner backend APIs