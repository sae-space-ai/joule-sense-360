"""Illustrative planning policy. No navigation safety claims."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Decision:
    action: str
    change_fraction: float
    reason: str

def plan(change_fraction: float | None) -> Decision:
    if change_fraction is None:
        return Decision("REQUEST_NEW_VIEW", -1.0, "No comparable visual evidence")
    if not (0 <= change_fraction <= 1):
        raise ValueError("change_fraction must be in [0,1]")
    if change_fraction > 0.10:
        return Decision("FLAG_CHANGE", change_fraction, "Significant image-level difference: human review")
    return Decision("ACCEPT_KNOWN", change_fraction, "No large pixel-level change detected; NOT route safety")
