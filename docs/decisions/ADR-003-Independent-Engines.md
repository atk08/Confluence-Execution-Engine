# ADR-003: Independent Analysis Engines

Status: Accepted

Date: July 2026

## Decision

Every analysis engine has exactly one responsibility.

Examples:

- Volume Profile Engine
- Anchored VWAP Engine
- Fair Value Gap Engine
- Market Context Engine

## Rationale

Single-responsibility engines are easier to test, replace, and improve.

## Consequences

Engines never calculate another engine's outputs.

They communicate only through standardized Institutional Evidence Objects.