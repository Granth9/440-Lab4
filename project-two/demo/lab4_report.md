# Lab 4 results

I checked this report against the [mini agent session](evidence/session.json) and
[skills audit](evidence/skills.jsonl). The live Ollama model was
`qwen2.5-coder:1.5b`. It selected the Lab 5 skill automatically, ran both Lab 4
scripts, and searched the AIMA MDP source. The first prompt scored 1.0 against
`rl-hyperparams`, above the 0.65 threshold. The agent needed follow-up prompts
to progress after Strategy 1. The model's report was incomplete, so Codex
verified the source and wrote this copy.

## Strategy 1 — Persistent context

`python3 strategy_1/main.py` exited with code 0. The loader reads
`strategy_1/CLAUDE.md` and `strategy_1/project_context.md`. The former contains
reusable project instructions, and the latter describes the AIMA repository
and the lab goals. The script displays the combined context on each run.

## Strategy 4 — Isolation through sub-agents

`python3 strategy_4/method4.py` exited with code 0.
`strategy_4/context_filter.py` gives both roles the project context, each role its
own notes, and each call its own task brief. The reviewer receives
`code_review_context.md` and the four AIMA source files
`grid_mdp.py`, `mdp.py`, `vacuum_agent.py`, and `xy_vacuum_environment.py`.
The researcher receives `research_context.md` and no source files.
`method4.py` combines the two reports. The two roles are deterministic Python
functions. The Ollama model is the outer agent running the demonstration.

## Lab 5 defaults and AIMA

| Setting | Lab 5 Q-learning skill | Lab 4 AIMA grid |
| --- | --- | --- |
| Living reward | −0.04 | −0.04 for nonterminal, traversable cells |
| Discount | 0.9 | `GridMDP` defaults to `gamma=.9` |
| Learning rate | 0.1 | AIMA's value and policy iteration routines use the model's transition probabilities |
| Exploration epsilon | 0.1 | AIMA's `value_iteration` uses `epsilon=0.001` as a stopping tolerance |

The evidence appears in `aima-python/aima/mdp.py` at the `GridMDP` constructor
(line 146), the 4×3 `sequential_decision_environment` (line 229), and the
value and policy iteration definitions (lines 250 and 285). The shared reward
and discount establish the comparison. The exploration and learning-rate
settings apply to the separate Lab 5 Q-learning implementation.
