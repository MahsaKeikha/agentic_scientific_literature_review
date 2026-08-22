# F90 | Agentic Scientific Literature Review | L3 Gold Standard | v1.0

A governed multi-agent reference system for reproducible scientific literature review, including question formulation, search strategy, screening, evidence synthesis, quality appraisal, uncertainty handling, and qualified human review.

## Review pipeline

- Review question formulation
- Reproducible search strategy
- Eligibility and screening
- Evidence synthesis
- Quality and risk-of-bias review

## Gold-standard research integrity

F90 is fail closed. Release requires reviewed search and eligibility protocols, traceable screening decisions, extraction and citation provenance, quality appraisal, reviewed synthesis methods, uncertainty review, and explicit qualified human approval.

Release is blocked for incomplete search strategies, unreviewed eligibility changes, incomplete screening traces, missing citation or extraction provenance, quality-appraisal gaps, ignored material heterogeneity, unaddressed publication bias, or overclaimed consensus.

The reference system cannot fabricate citations or study data, hide exclusion reasons, suppress material conflicts, or claim scientific consensus without adequate evidence and human review.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out literature-review suite.
