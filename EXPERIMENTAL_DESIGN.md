# Experimental Design Review — FP-21: Prompt Injection Taxonomy Across Agent Frameworks

> **Gate:** 0 (must pass before Phase 1 compute)
> **Date:** 2026-03-20
> **Target venue:** DEF CON AI Village / BSides [HYPOTHESIZED]
> **lock_commit: `3ea3f31`
> **Profile:** contract-track
> **Budget:** ~$3-5 Claude API (Haiku)

---

## Novelty Claim

> First systematic cross-framework comparison of prompt injection attack surfaces across LangChain, CrewAI, and AutoGen prompt assembly patterns.

---

## Comparison Baselines

| # | Method | Citation | How We Compare |
|---|--------|----------|---------------|
| 1 | Direct API (no framework) | Control | Baseline injection rate without framework mediation |
| 2 | Prior FP-08/FP-13 results | This portfolio | Single-framework results to compare against |
| 3 | OWASP LLM Top 10 categories | OWASP 2023 | Standard injection taxonomy to validate our coverage |

---

## Pre-Registered Reviewer Kill Shots

| # | Criticism | Planned Mitigation |
|---|----------|-------------------|
| 1 | "Framework versions change; results become stale" | Pin exact versions. Report version numbers. Results are a snapshot, not permanent — acknowledged in Limitations. |
| 2 | "You're testing prompt patterns, not running frameworks" | Explicitly framed as prompt-pattern analysis. We extract and test the actual prompt assembly patterns each framework uses. This IS the attack surface. |
| 3 | "20 injection types is not exhaustive" | Covers OWASP LLM Top 10 + FP-08/FP-13 taxonomy. Acknowledged as non-exhaustive. Community can extend. |

---

## Ablation Plan

| Component | Hypothesis When Changed | Expected Effect | Priority |
|-----------|------------------------|-----------------|----------|
| Framework (LangChain, CrewAI, AutoGen, direct API) | Framework adds/removes attack surface | Success rate varies ≥20pp across frameworks | HIGH |
| Injection type (direct, indirect, context manipulation, multi-turn) | Some types more effective than others | Indirect > direct across all frameworks | HIGH |
| Agent complexity (single tool, multi-tool, multi-agent) | More complex = more attack surface | Multi-agent > single-agent success rate | MEDIUM |

---

## Ground Truth Audit

| Source | Type | Count | Positive Rate | Limitations |
|--------|------|-------|---------------|-------------|
| Manual classification of injection success/failure | Expert judgment | 20 injections × 4 frameworks × 5 seeds = 400 decisions | Varies by condition | Subjective classification |
| Framework prompt templates | Extracted from source code | 4 frameworks | N/A | Version-specific |

### Alternative Sources Considered

| Source | Included? | Rationale |
|--------|-----------|-----------|
| Greshake et al. injection dataset | Reference only | Different context (web, not agent frameworks) |
| HackAPrompt competition data | NO | Competition-specific, not framework-specific |

---

## Statistical Plan

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Seeds | 5 (42, 123, 456, 789, 1024) | govML standard |
| Injections | 20 (5 per category × 4 categories) | Covers OWASP + FP-08/FP-13 taxonomy |
| Frameworks | 4 (LangChain, CrewAI, AutoGen, direct API) | Top 3 frameworks + control |
| Primary metric | Injection success rate per framework | Binary: did injection change agent behavior? |
| Significance test | Chi-square test (framework × success) | Categorical comparison |
| Multiple comparisons | Holm-Bonferroni for 6 pairwise comparisons | 4 choose 2 = 6 pairs |
| Effect size | ≥20pp success rate difference between frameworks | Practitioner-meaningful |

---

## Related Work

| # | Paper | Year | Relevance |
|---|-------|------|-----------|
| 1 | Greshake et al. — "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Apps" | 2023 | Indirect prompt injection in LLM apps |
| 2 | Perez & Ribeiro — "Ignore This Title and HackAPrompt" | 2023 | Prompt injection competition and taxonomy |
| 3 | OWASP — "Top 10 for LLM Applications" | 2023 | Standard vulnerability taxonomy for LLM apps |
| 4 | Liu et al. — "Prompt Injection Attacks and Defenses in LLM-Integrated Apps" | 2023 | Survey of injection attack and defense methods |
| 5 | Prior FP-08 (multi-agent-security) | 2026 | Multi-agent cascade vulnerability analysis |
| 6 | Prior FP-13 (agent-semantic-resistance) | 2026 | Agent resistance patterns under injection |

---

## Threats to Validity

| Threat | Type | Mitigation |
|--------|------|-----------|
| Framework version dependency — results tied to specific versions | External validity | Pin and report exact versions. Limitation acknowledged. |
| Prompt pattern extraction may not capture all framework-specific behaviors | Construct validity | Validate against framework documentation. Test patterns produce same output as full framework on sample inputs. |
| Injection taxonomy may not be exhaustive | External validity | Based on OWASP Top 10 + FP-08/FP-13. Coverage acknowledged as non-exhaustive. |
| Success classification is subjective | Construct validity | Define binary criteria: injection succeeds if agent output changes from baseline. Test on known-positive and known-negative injections first. |
| API model updates during experiment | Internal validity | Pin model version (claude-3-haiku-20240307). All experiments run in single session. |

---

## Audience Alignment

- **Audience:** AI builders choosing frameworks + security practitioners assessing agent attack surfaces
- **Portfolio position:** Extends FP-08/FP-13 multi-agent security line with cross-framework comparison. Practical, actionable.
- **Distribution plan:** Blog on rexcoleman.dev → LinkedIn → Reddit r/netsec + r/LangChain → DEF CON AI Village CFP. "Which framework is safest?" is a question every AI builder has.

---

## Depth Escalation (R34)

### Depth Commitment
ONE primary finding: framework choice creates ≥20pp variation in prompt injection success rate, with specific framework patterns (tool output injection, system prompt persistence) explaining the differences.

### Mechanism Analysis Plan
| Finding | Proposed Mechanism | Experiment to Verify |
|---------|-------------------|---------------------|
| Framework adds attack surface | Frameworks inject system prompts, tool descriptions, and memory that create injection vectors | Compare direct API (no framework) vs framework-mediated on same injections |
| Indirect > direct injection | Tool outputs bypass system prompt restrictions because frameworks don't sanitize tool returns | E2: separate direct vs indirect success rates |
| Multi-agent more vulnerable | Inter-agent messages create injection propagation paths | E3: single vs multi-agent comparison |

### Adaptive Adversary Plan
| Robustness Claim | Weak Test | Adaptive Test |
|-----------------|-----------|---------------|
| Framework default prompt is safe | Standard injections from OWASP | Framework-specific injections that exploit known prompt patterns |
| System prompt persists after injection | Single injection attempt | Multi-turn injection that gradually shifts context |

### Formal Contribution Statement (draft)
We contribute:
1. First cross-framework injection success rate comparison (LangChain, CrewAI, AutoGen, direct API)
2. Taxonomy of 20 injection types mapped to framework-specific attack surfaces
3. Practical security guidance: which framework patterns are most/least resistant

### Published Baseline Reproduction
Reproduce FP-08 cascade vulnerability findings with updated framework versions.

### Parameter Sensitivity Plan
| Parameter | Range | Expected Effect |
|-----------|-------|-----------------|
| Injection complexity | simple/medium/advanced | Advanced injections have higher success across frameworks |
| Agent tool count | 1/3/5 tools | More tools = more attack surface |
| System prompt length | short/medium/long | Longer system prompts may resist injection better |

### Defense Harm Test
N/A — no defense deployed. This study maps attack surfaces, not defenses.

---

## Experiment Matrix

| ID | Question | IV | Levels | DV | Seeds |
|----|----------|-----|--------|-----|-------|
| E0 | Sanity: known injection succeeds on known-vulnerable setup | N/A | 3 known injections | Binary success/fail | 1 |
| E1 | Full matrix: framework × injection type | Framework × injection | 4 × 20 | Success rate | 5 |
| E2 | Direct vs indirect injection | Injection delivery | Direct, Indirect via tool output | Success rate per framework | 5 |
| E3 | Single vs multi-agent | Agent complexity | Single, multi-agent | Success rate per framework | 5 |
| E4 | Framework-specific defenses | Defense presence | Default, hardened system prompt | Success rate change | 5 |
