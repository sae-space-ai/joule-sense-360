import numpy as np
import cv2
from joule.vision import verify_opencv5, inspect

def _jpg(a):
    ok,b=cv2.imencode(".jpg",a)
    assert ok
    return b.tobytes()

def test_opencv5_major():
    assert verify_opencv5().startswith("5.")

def test_blank_scene_requests_new_view():
    im=np.zeros((240,320,3),np.uint8)
    assert inspect(_jpg(im),_jpg(im))["status"]=="uncertain"

def test_textured_scene_aligns():
    rng=np.random.default_rng(100)
    a=rng.integers(0,256,(240,320,3),dtype=np.uint8)
    result=inspect(_jpg(a),_jpg(a))
    assert result["status"]=="aligned"
    assert result["change_fraction"]<0.05
