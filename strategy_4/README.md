# Strategy 4: Isolation via Sub-Agents

Run from the repository root:

```powershell
py strategy_4/method4.py
```

The orchestrator prepares separate allowlisted context bundles for a code reviewer and a researcher. It reads the existing AIMA vacuum/MDP source files and passes those files only to the code reviewer. The researcher receives only project/strategy context and its task brief. The orchestrator combines their reports.

The agents are deterministic Python functions, not LLM-backed agents. This keeps the demonstration dependency-free and makes the context split visible in the output.
