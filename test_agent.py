from joule.agent import decide

def test_missing_alignment_changes_action():
    assert decide({"status":"uncertain","change_fraction":None})["decision"]["action"]=="REQUEST_NEW_VIEW"

def test_large_difference_changes_action():
    assert decide({"status":"aligned","change_fraction":0.3})["decision"]["action"]=="FLAG_CHANGE_FOR_REVIEW"

def test_small_difference_does_not_claim_safe_route():
    msg=decide({"status":"aligned","change_fraction":0.02})
    assert msg["decision"]["action"]=="REPORT_NO_LARGE_VISUAL_CHANGE"
    assert msg["human_supervision_required"]
