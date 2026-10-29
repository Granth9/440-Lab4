# CS440 Lab 4 — Context-Engineering Strategies

This repository contains one project with demonstrations of Strategy 1 and Strategy 4, alongside the AIMA Python source repository.

## Strategy 1: Persistent context
- `strategy_1/CLAUDE.md`: persistent project instructions.
- `strategy_1/project_context.md`: reusable repository and lab context.
- `strategy_1/context_loader.py`: loads the two context files.
- `strategy_1/main.py`: runnable demonstration.

## Strategy 4: Isolation via sub-agents
- `strategy_4/method4.py`: orchestrates two specialized functions.
- `strategy_4/context_filter.py`: allowlists context files for each role.
- `strategy_4/agents/code_reviewer.py`: reviews a small set of relevant AIMA vacuum/MDP source files.
- `strategy_4/agents/researcher.py`: explains the architecture using only research context.
- `strategy_4/context/`: project, code-review, and research notes.

## Run the demonstrations

From this repository's root in PowerShell:

```powershell
py strategy_1/main.py
py strategy_4/method4.py
```

No extra packages are needed for these two demonstrations.

**Scope note:** The Strategy 4 agents are deterministic Python stand-ins used to demonstrate orchestration and context isolation. They do not call an LLM. Strategy 1's Python loader reads persistent context files but does not inject them into a ChatGPT session. The `aima-python/` folder is the source project being used as repository context; the lab code does not modify its application behavior.
