PROHIBITED = {"fabricate_citation", "hide_exclusion_reason", "claim_consensus_without_evidence"}


def check(action):
    if action in PROHIBITED:
        raise PermissionError(f"Blocked action: {action}")
    return {"allowed": True, "human_review_required": True}
