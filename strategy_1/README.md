# Strategy 1: Persistent Context

`CLAUDE.md` stores concise, persistent project instructions. `project_context.md` stores reusable facts about this repository and the lab. `context_loader.py` reads both files from this folder, and `main.py` demonstrates that the context can be loaded on demand.

Run from the repository root:

```powershell
py strategy_1/main.py
```

This Python demo proves that context is stored in files and can be loaded consistently. It does **not** automatically inject context into ChatGPT or another AI session. `CLAUDE.md` is a conventional instruction file for compatible coding tools; the Python loader is the runnable demonstration in this repository.
