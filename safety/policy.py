"""Fail-closed research-integrity policy for F90 literature review."""

PROHIBITED = {
    "fabricate_citation",
    "hide_exclusion_reason",
    "claim_consensus_without_evidence",
    "fabricate_study_data",
    "suppress_material_conflict",
}

REQUIRED_REVIEWS = (
    "review_question_reviewed",
    "search_strategy_reviewed",
    "eligibility_criteria_reviewed",
    "screening_trace_reviewed",
    "extraction_provenance_reviewed",
    "quality_appraisal_reviewed",
    "synthesis_method_reviewed",
    "uncertainty_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROHIBITED:
        return {"allowed": False, "reason": "research-integrity violation is outside system authority"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required literature-review control", "missing": missing}

    blockers = []
    if context.get("search_strategy_incomplete"):
        blockers.append("search strategy is not sufficiently reproducible")
    if context.get("eligibility_criteria_changed_unreviewed"):
        blockers.append("eligibility criteria changed without review")
    if context.get("screening_trace_incomplete"):
        blockers.append("screening decisions are not fully traceable")
    if context.get("citation_provenance_missing"):
        blockers.append("citation or extraction provenance missing")
    if context.get("quality_appraisal_gap"):
        blockers.append("study quality or risk of bias not adequately appraised")
    if context.get("heterogeneity_ignored"):
        blockers.append("material heterogeneity ignored in synthesis")
    if context.get("publication_bias_unaddressed"):
        blockers.append("publication bias not addressed")
    if context.get("consensus_overclaimed"):
        blockers.append("consensus or certainty overclaimed")

    if blockers:
        return {"allowed": False, "reason": "literature-review governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "review package approved after qualified human review"}


def check(action: str, context: dict | None = None) -> dict:
    """Backward-compatible policy entry point."""
    result = authorize(action, context)
    if action in PROHIBITED:
        raise PermissionError(f"Blocked action: {action}")
    return {**result, "human_review_required": True}
