from AGENTS.question_agent import run as question
from AGENTS.search_strategy_agent import run as search_strategy
from AGENTS.screening_agent import run as screening
from AGENTS.evidence_synthesis_agent import run as synthesis
from AGENTS.quality_review_agent import run as quality


def run(context):
    state = {"input": context, "stages": []}
    for name, fn in [("question", question), ("search_strategy", search_strategy), ("screening", screening), ("synthesis", synthesis), ("quality", quality)]:
        state["stages"].append({"stage": name, "output": fn(state)})
    state["status"] = "human_review_required"
    return state
