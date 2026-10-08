"""HTTP image-analysis endpoint deployable in an AWS container."""
from fastapi import FastAPI, UploadFile, File, HTTPException
from .vision import inspect,verify_opencv5
from .agent import decide

app=FastAPI(title="JOULE SENSE 360° — research visual processing", version="0.2.0")

@app.get("/health")
def health():
    try: version=verify_opencv5()
    except RuntimeError as exc: raise HTTPException(status_code=503,detail=str(exc))
    return {"status":"ok","opencv_version":version}

@app.post("/analyze")
async def analyze(reference: UploadFile=File(...), current: UploadFile=File(...)):
    try:
        a=await reference.read(8_000_001)
        b=await current.read(8_000_001)
        return decide(inspect(a,b))
    except (ValueError,RuntimeError) as exc:
        raise HTTPException(status_code=422,detail=str(exc))
