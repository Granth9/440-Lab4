from rl.grid_mdp import GridMDP
from rl.hyperparams import (
    DISCOUNT,
    EPISODES,
    EPSILON,
    LEARNING_RATE,
    LIVING_REWARD,
    SEED,
)
from rl.q_learning import QAgent, evaluate, train


def main():
    mdp = GridMDP(living_reward=LIVING_REWARD, discount=DISCOUNT)
    agent = QAgent(mdp, alpha=LEARNING_RATE, epsilon=EPSILON, seed=SEED)

    print("living reward:", LIVING_REWARD)
    print("discount:", DISCOUNT)
    print("learning rate:", LEARNING_RATE)
    print("epsilon:", EPSILON)
    print("episodes:", EPISODES)
    print()

    returns = train(agent, EPISODES)
    avg_last = sum(returns[-100:]) / 100
    avg_eval = evaluate(agent, 200)

    print("last 100 train avg:", round(avg_last, 3))
    print("greedy eval avg:", round(avg_eval, 3))
    print()
    print("policy:")
    print(mdp.policy_arrows(agent.policy()))


if __name__ == "__main__":
    main()
