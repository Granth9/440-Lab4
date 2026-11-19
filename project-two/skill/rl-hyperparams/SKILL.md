Triggers: Lab 4, Q-learning, reinforcement learning, RL hyperparameters, grid MDP

# RL hyperparams skill

## Lab 4 workflow

For a Lab 4 walkthrough, run these commands from the Lab 4 root in order, using one `run_shell` call per command.

1. `python3 strategy_1/main.py`
2. `python3 strategy_4/method4.py`

Use the results to complete the report.
- Summarize Strategy 1's persistent context and Strategy 4's role-specific context. Identify which role receives the AIMA source files.
- Compare the Lab 5 defaults below to the AIMA grid example. Search `aima-python/aima/mdp.py` for the `GridMDP` constructor, `sequential_decision_environment`, `value_iteration`, and `policy_iteration`. Use the constructor for the discount and the grid definition for the living reward. Keep the learning rate and epsilon scoped to Q-learning.
- For Lab 4, leave the source files intact.
- Write the observed results, commands, and comparison to `lab4_report.md`. Report any command failure as a failure and cite the relevant source paths.

## Lab 5 defaults

Use these defaults unless something is clearly broken:

- living reward: -0.04
- discount: 0.9
- learning rate: 0.1
- epsilon: 0.1

living reward is a small step cost so the agent finishes.
discount keeps future reward important.
learning rate 0.1 is fine on this small grid.
epsilon 0.1 explores a little but mostly exploits.

In the Lab 5 workspace, the values live in `rl/hyperparams.py` and `python3 -m rl.main` runs the training demo.
