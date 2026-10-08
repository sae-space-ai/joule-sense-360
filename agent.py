"""Explicit perception -> decision -> action policy, designed for audited traces."""
from __future__ import annotations
def decide(perception: dict) -> dict:
    fraction=perception.get("change_fraction")
    if perception.get("status") != "aligned" or fraction is None:
        action="REQUEST_NEW_VIEW"
        reason="Visual comparison could not be verified"
    elif fraction>=0.12:
        action="FLAG_CHANGE_FOR_REVIEW"
        reason="Aligned images differ beyond experimental threshold"
    else:
        action="REPORT_NO_LARGE_VISUAL_CHANGE"
        reason="No large change detected; hazards may still be present"
    return {"perception":perception,"decision":{"action":action,"reason":reason},
            "human_supervision_required":True}
