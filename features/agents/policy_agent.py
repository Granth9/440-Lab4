import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from rl.grid_mdp import GridMDP
from rl.hyperparams import DISCOUNT, EPISODES, EPSILON, LEARNING_RATE, LIVING_REWARD, SEED
from rl.q_learning import QAgent, evaluate, train


def run(context):
    mdp = GridMDP(living_reward=LIVING_REWARD, discount=DISCOUNT)
    agent = QAgent(mdp, alpha=LEARNING_RATE, epsilon=EPSILON, seed=SEED)
    train(agent, EPISODES)
    avg = evaluate(agent, 100)
    policy = mdp.policy_arrows(agent.policy())
    return (
        "policy agent\n"
        f"context files: {', '.join(context)}\n"
        f"greedy eval avg: {round(avg, 3)}\n"
        "policy:\n"
        + policy
    )
