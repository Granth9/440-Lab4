# Strategy 4: Isolation via Sub-Agents (Python)

This folder is a Python demonstration of the Strategy 4 architecture shown in the CS440 Context Engineering slides:
- Main agent / orchestrator: receives a task and delegates it.
- Context filter: gives each sub-agent only the context needed for its role.
- Specialized sub-agents: a code reviewer and a researcher return separate findings.
- Orchestrator: combines the findings into one report.

## Files

- `method4.py` — orchestration entry point
- `context_filter.py` — allowlisted context selection per agent
- `agents/code_reviewer.py` — reviews vacuum robot code context
- `agents/researcher.py` — checks architecture/assignment context
- `context/project_context.md` — shared project facts
- `context/code_review_context.md` — code-review-specific facts
- `context/research_context.md` — research-specific facts

## Run

Requires Python 3.10+; no third-party packages are needed.

```bash
python method4.py
```

To review the real project files, run from this folder and pass file paths:

```bash
python method4.py --env-path ../vacuum_env.py --agent-path ../q_learning.py --main-path ../main.py
```

The current agents are deterministic, rule-based demonstration agents. They demonstrate delegation and context isolation without requiring an API key. They are not LLM-powered agents. If the assignment expects agents to call an LLM, this scaffold should be upgraded to use the model/API specified by your instructor.

## Context isolation

The code reviewer receives only code-oriented context and the supplied source code. The researcher receives only project/assignment context. The code reviewer is not given the researcher's context, and the researcher is not given source code unless explicitly passed through its filter. The orchestrator receives both agents' final reports, not their entire private input bundles.

## Important scope note

This is a Strategy 4 component only. It does not change the existing vacuum environment or Q-learning code. Strategy 1 persistent-memory files can be added separately by your partner.
