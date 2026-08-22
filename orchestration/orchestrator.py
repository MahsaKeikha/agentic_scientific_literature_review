from AGENTS.evidence_synthesis_agent import run as synthesis
from AGENTS.quality_review_agent import run as quality
from AGENTS.question_agent import run as question
from AGENTS.screening_agent import run as screening
from AGENTS.search_strategy_agent import run as search_strategy
from safety.policy import authorize


def run(context: dict) -> dict:
    """Run the literature-review pipeline and apply fail-closed governance."""
    state = {"system": "F90", "input": context, "stages": []}
    for name, fn in [
        ("question", question),
        ("search_strategy", search_strategy),
        ("screening", screening),
        ("synthesis", synthesis),
        ("quality", quality),
    ]:
        state["stages"].append({"stage": name, "output": fn(state)})

    governance = authorize("review_release", context)
    state.update(
        {
            "status": "human_review_required",
            "human_review_required": True,
            "governance": governance,
            "release_allowed": governance["allowed"],
            "autonomous_consensus_authority": False,
        }
    )
    return state
