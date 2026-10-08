"""Actual OpenCV 5 image decoding, alignment and change analysis. NOT navigation safety."""
from __future__ import annotations
import cv2
import numpy as np

def verify_opencv5() -> str:
    version = cv2.__version__
    if version.split('.')[0] != '5':
        raise RuntimeError(f"OpenCV 5 required, got {version}")
    return version

def inspect(reference_bytes: bytes, current_bytes: bytes) -> dict:
    verify_opencv5()
    def decode(raw: bytes):
        if len(raw)>8_000_000: raise ValueError("Image too large")
        im=cv2.imdecode(np.frombuffer(raw,dtype=np.uint8), cv2.IMREAD_COLOR)
        if im is None: raise ValueError("Invalid image")
        if im.shape[0]*im.shape[1]>8_000_000: raise ValueError("Too many image pixels")
        return im
    ref=decode(reference_bytes)
    cur=decode(current_bytes)
    # Align with ORB + RANSAC; do not falsely claim scene invariance if alignment fails.
    gray_ref=cv2.cvtColor(ref,cv2.COLOR_BGR2GRAY)
    gray_cur=cv2.cvtColor(cur,cv2.COLOR_BGR2GRAY)
    orb=cv2.ORB_create(nfeatures=1200)
    k1,d1=orb.detectAndCompute(gray_ref,None)
    k2,d2=orb.detectAndCompute(gray_cur,None)
    matches=[]
    aligned=None
    inliers=0
    if d1 is not None and d2 is not None:
        bf=cv2.BFMatcher(cv2.NORM_HAMMING)
        pairs=bf.knnMatch(d1,d2,k=2)
        matches=[m for pair in pairs if len(pair)==2 for m,n in [pair] if m.distance<0.75*n.distance]
    if len(matches)>=10:
        src=np.float32([k2[m.trainIdx].pt for m in matches]).reshape(-1,1,2)
        dst=np.float32([k1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
        h,mask=cv2.findHomography(src,dst,cv2.RANSAC,4.0)
        if h is not None and mask is not None:
            inliers=int(mask.sum())
            if inliers>=8:
                aligned=cv2.warpPerspective(cur,h,(ref.shape[1],ref.shape[0]))
    if aligned is None:
        return {"opencv_version":cv2.__version__,"status":"uncertain","feature_matches":len(matches),
                "inliers":inliers,"change_fraction":None,"note":"Cannot verify geometric alignment"}
    diff=cv2.absdiff(gray_ref, cv2.cvtColor(aligned,cv2.COLOR_BGR2GRAY))
    blurred=cv2.GaussianBlur(diff,(5,5),0)
    # Illustrative threshold, not calibrated to hazard or distance estimates.
    change=float(np.mean(blurred>35))
    return {"opencv_version":cv2.__version__,"status":"aligned","feature_matches":len(matches),
            "inliers":inliers,"change_fraction":round(change,5),
            "note":"Image-level change score only; not a clearance or distance guarantee"}
