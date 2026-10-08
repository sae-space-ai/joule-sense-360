# JOULE SENSE 360°
**Generative Spatial Memory & Agentic Vision for Accessibility**

Hackathon research prototype — **NOT a certified mobility or obstacle-avoidance device**. Never use outputs as the sole basis for navigation decisions.

## Mission
Demonstrate **OpenCV 5 + a meaningful AWS component**, active perception, personalized opt-in spatial memory, uncertainty reporting, and measurable edge/cloud efficiency. Future hardware: JOULE PIN; current priority: reproducible prototype.

## Repo status (2026-10-08)
Initial scaffolding only. No validated detection, distance estimation, mobile application, wearable hardware, AWS deployment, COOL benchmarks, or user trials are claimed.

## Local setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e '.[dev]'
python -m pytest -q
python -m joule.demo
```
Requires Python 3.11+; `opencv-python-headless==5.0.0.93` target from PyPI (confirm wheel for platform). The import checks the required major version.

## Roadmap
1. Implement reproducible OpenCV 5 image comparison and record uncertainty.
2. Close the perception → decision → action → verification loop, with test traces.
3. Add explicit opt-in spatial memory and delete/export controls.
4. Implement calibrated distance estimates only with suitable depth information, no fabricated meters.
5. AWS ECS/Graviton workload + S3 evidence + metrics, with secrets outside code.
6. Compare memoryless / static memory / active memory, and performance/cost.
7. Evaluate COOL on ARM if available, proving the actual workload.
8. Accessible demo, technical report, short video, security and failure cases.

Read [QWEN.md](QWEN.md), [docs/requirements.md](docs/requirements.md), and [docs/acceptance.md](docs/acceptance.md).
