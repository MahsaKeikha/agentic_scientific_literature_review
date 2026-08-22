from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
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


def test_complete_review_can_release_package():
    result = run(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_consensus_authority"] is False


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_fabricated_citation_is_never_authorized():
    assert authorize("fabricate_citation", valid_context())["allowed"] is False


def test_incomplete_search_strategy_blocks_release():
    context = valid_context()
    context["search_strategy_incomplete"] = True
    assert run(context)["release_allowed"] is False


def test_unreviewed_eligibility_change_blocks_release():
    context = valid_context()
    context["eligibility_criteria_changed_unreviewed"] = True
    assert run(context)["release_allowed"] is False


def test_missing_provenance_blocks_release():
    context = valid_context()
    context["citation_provenance_missing"] = True
    assert run(context)["release_allowed"] is False


def test_heterogeneity_ignored_blocks_release():
    context = valid_context()
    context["heterogeneity_ignored"] = True
    assert run(context)["release_allowed"] is False


def test_consensus_overclaim_blocks_release():
    context = valid_context()
    context["consensus_overclaimed"] = True
    assert run(context)["release_allowed"] is False
