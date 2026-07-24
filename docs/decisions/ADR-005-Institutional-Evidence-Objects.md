# ADR-005: Institutional Evidence Objects

Status: Accepted

Date: July 2026

## Decision

All analysis engines return the same standardized data structure known as an Institutional Evidence Object (IEO).

## Rationale

A common object model simplifies integration between engines and ensures consistent processing throughout the platform.

## Consequences

Every IEO contains:

- Identifier
- Type
- Price
- Quality
- Reliability
- Integrity (if applicable)
- Weight
- Supporting Evidence
- Metadata

New evidence types must conform to the IEO specification before being integrated into the engine.