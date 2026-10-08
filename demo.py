"""Tiny synthetic illustration; full agent loop and AWS are future work."""
import json
import numpy as np
from .vision import changed_fraction, opencv_version
from .agent import plan

def main() -> None:
    baseline = np.zeros((100, 100, 3), dtype=np.uint8)
    altered = baseline.copy()
    altered[20:70, 20:70] = 255
    result = changed_fraction(baseline, altered)
    print(json.dumps({"opencv_version": opencv_version(), "decision": plan(result).__dict__}, indent=2))

if __name__ == "__main__":
    main()
