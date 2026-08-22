from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "scientific literature review",
    "review_question_reviewed": True,
    "search_strategy_reviewed": True,
    "eligibility_criteria_reviewed": True,
    "screening_trace_reviewed": True,
    "extraction_provenance_reviewed": True,
    "quality_appraisal_reviewed": True,
    "synthesis_method_reviewed": True,
    "uncertainty_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
