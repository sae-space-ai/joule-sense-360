# Qwen Code — permanent project instructions
You are lead IMPLEMENTATION agent, working under the **JOULE** product architecture; the human owner approves scope, costs, data access, deployment and risky actions. You are not authorized to claim certifications, tests, AWS deployments or hardware that have not occurred.

Read @README.md, @docs/requirements.md, @docs/acceptance.md, and @docs/safety.md before modifying code.

## Priorities
P0: runnable and tested OpenCV **5** visual pipeline, meaningful AWS workload, genuine visual-result-dependent agent loop and reproducible tests.
P1: opt-in spatial memory, change detection, quantitative baselines, cost/latency logs, accessible demonstration.
P2: COOL/Graviton comparison if reproducible, cross-platform connectivity and miniaturized pin as separately labeled future work.

## Engineering rules
- Work in small commits; show files changed, commands run, test results, remaining gaps.
- Python 3.11+, typed interfaces, pytest. Keep reproducibility and pinned dependencies.
- No made-up spatial distances, success rates, measurements, OpenCV results, or AWS logs.
- Never generate route-safety guarantees. Fail closed on uncertainty / sensor loss. No safety-critical autonomous navigation.
- Don't use identifiable recordings without consent. No default cloud uploads; encrypt sensitive data, implement deletion.
- Keep camera/voice/network permissions minimal; don't hardcode AWS secrets or biometric identification.
- Do not claim a prototype drawing is actual hardware. In documentation label planned vs implemented.
- For optional AWS changes, generate infrastructure-as-code and a cost estimate before requesting approval to deploy.
- Always run tests after changes. Record exact OpenCV version runtime and deployment evidence.

## FIRST TASK
Implement deterministic comparison on two test images using OpenCV 5 feature matching/change detection; demonstrate a visual output switching the agent's next action between ACCEPT_KNOWN, REQUEST_NEW_VIEW and FLAG_CHANGE. Supply a machine-readable decision trace, pytest coverage, runbook, and benchmark script. Stop before any AWS deployment and ask for approval.
