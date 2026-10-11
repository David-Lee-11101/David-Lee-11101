<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
  <img alt="David Lee — Java backend engineer building RPC frameworks and concurrent systems" src="./assets/hero-light.svg" width="100%">
</picture>

I build backend systems close to the infrastructure boundary: network transport, request correlation, service discovery, concurrent scheduling, rule analysis, recovery, and the tooling required to make those systems inspectable.

My current portfolio is organized around three engineering threads.

## Selected engineering

### [Handwritten Netty RPC](https://github.com/David-Lee-11101/Handwritten-Netty-RPC)

A compact Java RPC framework built from first principles with Netty, dynamic proxies, reflection-based invocation, request correlation, deadlines, reconnect behavior, and explicit channel lifecycle management. The project is designed to make transport and failure semantics easy to inspect.

### [SmartService Discovery RPC](https://github.com/David-Lee-11101/SmartService-Discovery-RPC)

The public anchor for a multi-repository IoT automation series. Its Java modules cover service contracts, ZooKeeper registration and discovery, Netty transport, provider exposure, and consumer-side proxies.

The surrounding suite explores distinct parts of the same problem:

- [SmartRule Concurrency Scheduler](https://github.com/David-Lee-11101/SmartRule-Concurrency-Scheduler) — deterministic concurrent rule scheduling and action-arrival simulation.
- [SmartRule Conflict Analyzer](https://github.com/David-Lee-11101/SmartRule-Conflict-Analyzer) — reproducible rule conflict, dependency, and Apriori research.
- [SmartService Automate Generator](https://github.com/David-Lee-11101/SmartService-Automate-Generator) — service scaffolding and code-generation experiments.
- [SmartRule Automate Composer](https://github.com/David-Lee-11101/SmartRule-Automate-Composer) — visual rule composition and automation-toolchain research.

### [Imperium](https://github.com/David-Lee-11101/Imperium)

An experimental governed-agent workflow MVP built with Java 21, Spring Boot, React, MySQL, and event-driven workers. It represents deliberation, veto review, human approval, delegated execution, recovery, audit, and archive stages as explicit workflow state.

## Engineering principles

- Make failure behavior and lifecycle ownership explicit.
- Prefer reproducible demonstrations over unsupported performance claims.
- Keep architecture visible through small examples, diagrams, and tests.
- Treat experimental software honestly while improving it toward reliable systems.

## Open-source study

I maintain a [personal fork of oh-my-codex](https://github.com/David-Lee-11101/oh-my-codex) for local study and experimentation. The original project and authorship belong to the [upstream repository](https://github.com/Yeachan-Heo/oh-my-codex).
