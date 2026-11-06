# RL hyperparams skill

Use these defaults unless something is clearly broken:

- living reward: -0.04
- discount: 0.9
- learning rate: 0.1
- epsilon: 0.1

living reward is a small step cost so the agent finishes.
discount keeps future reward important.
learning rate 0.1 is fine on this small grid.
epsilon 0.1 explores a little but mostly exploits.

Values live in rl/hyperparams.py. Run: python3 -m rl.main
