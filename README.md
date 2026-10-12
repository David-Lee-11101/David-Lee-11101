<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
  <img alt="David Lee — independent research in smart home edge computing" src="./assets/hero-light.svg" width="100%">
</picture>

I build Java systems for networked automation and independent research in smart home edge computing. My work connects bounded RPC transport, typed computation graphs, traffic-shape profiling, concurrent scheduling, and service lifecycle management.

## Smart Home Edge Computing System

[System hub](https://github.com/David-Lee-11101/SmartHome-Edge-Computing-System) · [Architecture and causal integration](https://github.com/David-Lee-11101/SmartHome-Edge-Computing-System/blob/main/docs/RUNNER.md)

Five components form one engineering system: Management brings providers into service, Logic builds typed invocations, Communication carries calls, Profiling supplies traffic-shape evidence, and the Scheduler authorizes execution.

| Component | Role in the system |
| --- | --- |
| [Communication](https://github.com/David-Lee-11101/Smart-Home-Communication) | Lightweight Netty RPC with bounded calls, request correlation, and payload-free encoded-frame telemetry |
| [Logic Engine](https://github.com/David-Lee-11101/SmartHome-Logic-Engine) | Typed service invocation and calculation graphs: local catalogs, signatures, arithmetic, and record-field selection |
| [Traffic Profiling](https://github.com/David-Lee-11101/SmartHome-Traffic-Profiling) | Direction/encoded-length medoids and edit-distance classification of known, anomalous, ambiguous, and unknown traces |
| [ThreadSafe Scheduler](https://github.com/David-Lee-11101/SmartHome-ThreadSafe-Scheduler) | Evidence-based execution decisions persisted before actions, ordered resource locks, and owned cooperative cancellation |
| [Integrated Logic Management](https://github.com/David-Lee-11101/SmartHome-Integrated-Logic-Management) | Local definitions, template generation, provider lifecycle management, and independent state/evidence readback |

The service generator belongs to Integrated Logic Management; its historical repository preserves the development record. The [system runner](https://github.com/David-Lee-11101/SmartHome-Edge-Computing-System/blob/main/docs/RUNNER.md) documents the causal path from a generated provider through invocation, profiling, a persisted scheduling decision, and independent state readback, with revision pins and reproducible verification.

## Agent governance research

[Senate-Agent-Orchestration](https://github.com/David-Lee-11101/Senate-Agent-Orchestration) explores a Roman Senate inspired framework for deliberation, veto review, execution authority, recovery, and audit. Its Java and React workflow MVP is an incomplete foundation for that framework. The [proposal and boundaries](https://github.com/David-Lee-11101/Senate-Agent-Orchestration/blob/main/docs/SENATE_PROPOSAL.md) distinguish implemented workflow pieces from planned multiagent coordination.

## How I work

- Make failure behavior and lifecycle ownership explicit.
- Preserve experimental provenance and distinguish new tests from historical results.
- Keep architecture inspectable through small demonstrations and reviewable evidence.
- Treat privacy and rights as part of research publication.

Public visibility does not grant a general reuse license. Repository-specific notices and third-party licenses govern their respective content.

I also maintain a [personal oh-my-codex fork](https://github.com/David-Lee-11101/oh-my-codex) for tooling exploration. Upstream authorship belongs to [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex).
