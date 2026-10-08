from joule.agent import plan

def test_no_evidence_requests_new_view():
    assert plan(None).action == "REQUEST_NEW_VIEW"

def test_change_prompts_review():
    assert plan(0.25).action == "FLAG_CHANGE"

def test_low_change_not_safety_claim():
    decision=plan(0.01)
    assert decision.action == "ACCEPT_KNOWN"
    assert "NOT route safety" in decision.reason
