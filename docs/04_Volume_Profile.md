# Volume Profile Engine Specification

**Version:** 1.0
**Status:** Draft

---

# Purpose

The Volume Profile Engine measures how the market has conducted its auction.

It identifies where buyers and sellers have accepted value, rejected value, and left inefficient price areas.

The engine does not generate buy or sell signals.

Its responsibility is to describe the auction objectively.

---

# Objective

The engine identifies institutional price levels including:

- Point of Control (POC)
- Value Area High (VAH)
- Value Area Low (VAL)
- High Volume Nodes (HVNs)
- Low Volume Nodes (LVNs)

Each level is evaluated for quality before being passed to the Confluence Engine.

---

# Core Principle

Not all POCs are equal.

Not all HVNs are equal.

Not all LVNs are equal.

Every institutional level receives a Quality Score before contributing to the Institutional Confidence Score.
---

# Evidence Model

The Volume Profile Engine does not generate trade signals.

Instead, it produces evidence.

Each piece of evidence is assigned a quality score and supporting metadata.

This evidence is passed to the Institutional Confidence Engine for final evaluation.

---

# Evidence Types

The engine evaluates the following institutional evidence:

- Point of Control (POC)
- High Volume Nodes (HVNs)
- Low Volume Nodes (LVNs)
- Value Area High (VAH)
- Value Area Low (VAL)

Each evidence object is scored independently.

---

# Evidence Object

Every piece of evidence follows the same structure.

Example:

Type:
POC

Price:
118250

Quality:
93

Integrity:
100

Confidence:
High

Evidence:

- Untouched
- High Volume
- Strong Acceptance
- Three Historical Reactions

Metadata:

- Distance from Current Price
- Age
- Session Type