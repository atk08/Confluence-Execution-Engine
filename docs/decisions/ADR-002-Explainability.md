# ADR-002: Explainable Decisions

Status: Accepted

Date: July 2026

## Decision

Every Institutional Confidence Score must be fully explainable.

Every point awarded by the engine must be traceable to supporting evidence.

## Rationale

Black-box scores reduce user trust.

Transparent scoring allows traders to understand why the engine reached its conclusion.

## Consequences

Every score includes:

- Evidence
- Quality
- Reliability
- Confidence
- Metadata

The Explanation Engine never invents explanations.

It only describes evidence already produced by previous engines.