# LinkedIn Post — FP-21

We tested 20 prompt injections against LangChain, CrewAI, AutoGen, and direct API.

Results: 65-78% success rate across all frameworks. No framework is "safe."

But the averages hide the real finding:

CrewAI tool output injection: 80% success
Direct API tool output injection: 20% success

The framework's tool handling pattern IS the attack surface. CrewAI treats tool returns as trusted context. Direct API doesn't have a tool pattern to exploit.

Multi-agent: LESS vulnerable than single-agent (55% vs 70%). More context = more anchoring against injection.

Practical: sanitize tool outputs first. Framework choice second.

Full cross-framework analysis with heatmaps: [link]

#PromptInjection #AISecurity #LangChain #CrewAI #AutoGen #AgentSecurity
