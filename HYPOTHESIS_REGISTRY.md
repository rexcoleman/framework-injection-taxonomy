# HYPOTHESIS REGISTRY — FP-21 Framework Injection Taxonomy

> **Project:** FP-21
> **Created:** 2026-03-20
> **Status:** PENDING (0/4 resolved)
> **Lock commit:** TBD
> **Lock date:** 2026-03-20

---

## H-1: Framework-mediated agents are MORE vulnerable than direct API calls

| Field | Value |
|-------|-------|
| **Statement** | Agents using LangChain/CrewAI/AutoGen have higher injection success rates than direct API calls because frameworks add attack surface (system prompts, tool descriptions, memory). |
| **Prediction** | success_rate(framework) > success_rate(direct_API) by ≥20pp |
| **Falsification** | If framework success rate ≤ direct API, frameworks add defense, not attack surface. |
| **Status** | PENDING |
| **Linked Experiment** | E1 |

---

## H-2: Injection success rate varies ≥20pp across frameworks

| Field | Value |
|-------|-------|
| **Statement** | The three frameworks (LangChain, CrewAI, AutoGen) have significantly different injection success rates due to different prompt assembly patterns. |
| **Prediction** | max(framework_rates) - min(framework_rates) ≥ 20pp |
| **Falsification** | If rates are within 20pp, framework choice doesn't meaningfully affect security. |
| **Status** | PENDING |
| **Linked Experiment** | E1 |

---

## H-3: Indirect injection (via tool output) has higher success rate than direct injection

| Field | Value |
|-------|-------|
| **Statement** | Injections delivered through simulated tool outputs succeed more often than direct user-message injections, because frameworks don't sanitize tool returns. |
| **Prediction** | success_rate(indirect) > success_rate(direct) by ≥15pp across all frameworks |
| **Falsification** | If direct ≥ indirect, tool output handling is not a significant attack vector. |
| **Status** | PENDING |
| **Linked Experiment** | E2 |

---

## H-4: Multi-agent frameworks are more vulnerable than single-agent

| Field | Value |
|-------|-------|
| **Statement** | CrewAI (multi-agent) has higher injection success rate than LangChain (single-agent) because inter-agent messages create injection propagation paths. |
| **Prediction** | success_rate(CrewAI) > success_rate(LangChain) by ≥15pp |
| **Falsification** | If single ≥ multi, inter-agent communication does not amplify injection risk. |
| **Status** | PENDING |
| **Linked Experiment** | E3 |

---

## Summary

| ID | Statement (short) | Prediction | Status |
|----|-------------------|-----------|--------|
| H-1 | Frameworks add attack surface | ≥20pp over direct API | PARTIALLY SUPPORTED (LangChain +3pp only) |
| H-2 | Frameworks differ by ≥20pp | max - min ≥ 20pp | NOT SUPPORTED (13pp range) |
| H-3 | Indirect > direct injection | ≥15pp difference | FRAMEWORK-DEPENDENT (CrewAI +40pp, Direct API -60pp) |
| H-4 | Multi-agent more vulnerable | CrewAI > LangChain ≥15pp | NOT SUPPORTED (reversed: -15pp) |
