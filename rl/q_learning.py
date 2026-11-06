import random
from collections import defaultdict


class QAgent:
    def __init__(self, mdp, alpha=0.1, epsilon=0.1, seed=None):
        self.mdp = mdp
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = mdp.gamma
        self.rng = random.Random(seed)
        self.Q = defaultdict(float)

    def best_action(self, s):
        acts = self.mdp.actions(s)
        if acts == [None]:
            return None
        best = max(self.Q[(s, a)] for a in acts)
        choices = [a for a in acts if self.Q[(s, a)] == best]
        return self.rng.choice(choices)

    def pick_action(self, s, explore=True):
        acts = self.mdp.actions(s)
        if acts == [None]:
            return None
        if explore and self.rng.random() < self.epsilon:
            return self.rng.choice(acts)
        return self.best_action(s)

    def update(self, s, a, r, s2):
        if a is None:
            self.Q[(s, None)] = r
            return

        if s2 in self.mdp.terminals:
            future = self.mdp.R(s2)
        else:
            future = max(self.Q[(s2, a2)] for a2 in self.mdp.actions(s2))

        old = self.Q[(s, a)]
        self.Q[(s, a)] = old + self.alpha * (r + self.gamma * future - old)

    def policy(self):
        return {s: self.best_action(s) for s in self.mdp.states}


def step(mdp, s, a, rng):
    outcomes = mdp.T(s, a)
    x = rng.random()
    total = 0.0
    for p, s2 in outcomes:
        total += p
        if x < total:
            return s2
    return outcomes[-1][1]


def run_episode(agent, explore=True, learn=True):
    mdp = agent.mdp
    s = mdp.init
    total = 0.0

    while True:
        r = mdp.R(s)
        total += r
        a = agent.pick_action(s, explore=explore)

        if a is None:
            if learn:
                agent.update(s, None, r, s)
            break

        s2 = step(mdp, s, a, agent.rng)
        if learn:
            agent.update(s, a, r, s2)
        s = s2

    return total


def train(agent, episodes):
    returns = []
    for _ in range(episodes):
        returns.append(run_episode(agent, explore=True, learn=True))
    return returns


def evaluate(agent, episodes=100):
    total = 0.0
    for _ in range(episodes):
        total += run_episode(agent, explore=False, learn=False)
    return total / episodes
