# Backend API Specification

Version: 1.0

Status: Draft

---

# Philosophy

The Backend API exposes the Confluence Engine to all client applications.

Clients never calculate scores.

Clients never calculate evidence.

Clients only request analysis and display results.

The backend remains the single source of truth.

---

# Design Principles

- Stateless
- Versioned
- Deterministic
- Explainable
- Extensible

Every response must be reproducible.

---

# Primary Resources

The API exposes:

- Assets
- Evidence Objects
- Confluence Zones
- Institutional Confidence Scores
- Trade Plans
- Research Results
- Engine Metadata

---

# Response Standard

Every endpoint returns:

{
    success,
    version,
    timestamp,
    data,
    metadata
}

Errors follow the same structure.