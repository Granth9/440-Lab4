# CS440 Lab 4

Q-learning on the 4x3 grid, plus 3 portable features: skills, hooks, and sub-agents.
These run with plain Python/bash so they work in any IDE. Did not use MCP.

## Hyperparameters

| name | value |
|------|-------|
| living reward | -0.04 |
| discount | 0.9 |
| learning rate | 0.1 |
| epsilon | 0.1 |

Set in `rl/hyperparams.py`.

## Run the RL solution

```bash
python3 -m rl.main
```

## Run the 3 features

```bash
python3 features/demo.py
```

Or one at a time:

```bash
python3 features/skills/load_skill.py
python3 features/hooks/run_with_hook.py
python3 features/agents/orchestrator.py
```

## Layout

```
rl/                 Q-learning solution
features/skills/    skill file + loader
features/hooks/     pre-run hook
features/agents/    two sub-agents + orchestrator
```
