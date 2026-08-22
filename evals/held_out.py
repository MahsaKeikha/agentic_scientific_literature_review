from orchestration.orchestrator import run


def base():
    return {
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "search_strategy_incomplete": True}, False),
    ({**base(), "eligibility_criteria_changed_unreviewed": True}, False),
    ({**base(), "screening_trace_incomplete": True}, False),
    ({**base(), "citation_provenance_missing": True}, False),
    ({**base(), "quality_appraisal_gap": True}, False),
    ({**base(), "heterogeneity_ignored": True}, False),
    ({**base(), "consensus_overclaimed": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
