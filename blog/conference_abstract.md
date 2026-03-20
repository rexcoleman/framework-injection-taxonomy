# Conference Abstract — FP-21

**Title:** Cross-Framework Prompt Injection Rates: LangChain, CrewAI, and AutoGen Compared
**Target venue:** DEF CON AI Village / BSides [HYPOTHESIZED]
**Authors:** Rex Coleman, Singularity Cybersecurity LLC

## Abstract (250 words)
We present the first systematic cross-framework comparison of prompt injection success rates, testing 20 injection payloads across LangChain, CrewAI, AutoGen, and direct API prompt patterns. Injection success ranges from 65% (AutoGen) to 78% (LangChain), with framework choice creating 13pp variation — less than expected. The dominant factor is injection delivery method: CrewAI shows 80% indirect (tool output) success vs 40% direct, while direct API shows the opposite (20% indirect, 80% direct). Framework tool output handling patterns determine indirect injection viability. Multi-agent CrewAI is 15pp LESS vulnerable than single-agent, contrary to the assumption that more agents means more attack surface.

**Keywords:** prompt injection, agent frameworks, LangChain, CrewAI, AutoGen, AI security

## Author Bio
**Rex Coleman** is the founder of Singularity Cybersecurity LLC. Research spans security OF AI (multi-agent security, prompt injection) and security FROM AI (watermark robustness, AI-generated content). Previously at FireEye/Mandiant. MS CS Georgia Tech (ML). Securing AI from the architecture up.
