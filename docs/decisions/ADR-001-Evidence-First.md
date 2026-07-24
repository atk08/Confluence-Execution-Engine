# ADR-001: Evidence First Architecture

Status: Accepted

Date: July 2026

## Decision

The Confluence Engine evaluates institutional evidence rather than technical indicators.

Indicators are treated as sources of evidence, not trading signals.

## Rationale

Indicators frequently disagree because they measure different market characteristics.

The engine should determine how strongly independent evidence agrees rather than count indicator signals.

This creates a more objective and explainable system.

## Consequences

Every engine returns Institutional Evidence Objects (IEOs).

The Institutional Confidence Score is derived from evidence, not indicators.

Future indicators may be added without changing the architecture.