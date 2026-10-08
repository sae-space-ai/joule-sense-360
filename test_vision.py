import numpy as np
import pytest
from joule.vision import changed_fraction, opencv_version

def test_opencv5_is_required():
    assert opencv_version().startswith("5.")

def test_synthetic_change():
    a=np.zeros((20,20,3),dtype=np.uint8)
    b=a.copy()
    b[:10,:10]=255
    assert changed_fraction(a,b)==pytest.approx(0.25)

def test_shape_error():
    with pytest.raises(ValueError):
        changed_fraction(np.zeros((2,2,3),dtype=np.uint8),np.zeros((3,3,3),dtype=np.uint8))
