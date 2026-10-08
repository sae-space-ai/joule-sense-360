"""Version guard and OpenCV-backed, descriptive frame difference. Not calibrated depth."""
from __future__ import annotations
import numpy as np

def opencv_version() -> str:
    import cv2
    version = cv2.__version__
    if int(version.split(".")[0]) != 5:
        raise RuntimeError(f"OpenCV 5 required; installed {version}")
    return version

def changed_fraction(a: np.ndarray, b: np.ndarray, threshold: int = 25) -> float:
    import cv2
    opencv_version()
    if a.shape != b.shape or a.ndim != 3 or a.shape[2] != 3:
        raise ValueError("Equal-size BGR images required")
    ga = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    gb = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    delta = cv2.absdiff(ga, gb)
    return float(np.count_nonzero(delta > threshold) / delta.size)
