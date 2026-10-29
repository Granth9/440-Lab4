from __future__ import annotations

import random
from typing import Dict, List, Tuple

from vacuum_env import Action, VacuumEnvironment

State = Tuple[int, int]


class QLearningAgent:
    def __init__(self, env: VacuumEnvironment, alpha: float, gamma: float, epsilon: float) -> None:
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table: Dict[State, Dict[Action, float]] = {}

    def ensure_state(self, state: State) -> None:
        if state not in self.q_table:
            self.q_table[state] = {action: 0.0 for action in self.env.ACTIONS}

    def choose_action(self, state: State) -> Action:
        self.ensure_state(state)
        if random.random() < self.epsilon:
            return random.choice(self.env.ACTIONS)
        return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state: State, action: Action, reward: float, next_state: State, done: bool) -> None:
        self.ensure_state(state)
        self.ensure_state(next_state)

        current_q = self.q_table[state][action]
        best_next_q = max(self.q_table[next_state].values()) if not done else 0.0
        updated_q = current_q + self.alpha * (reward + self.gamma * best_next_q - current_q)
        self.q_table[state][action] = updated_q

    def train(self, episodes: int, max_steps_per_episode: int) -> List[float]:
        rewards: List[float] = []

        for _ in range(episodes):
            state = self.env.reset()
            total_reward = 0.0

            for _ in range(max_steps_per_episode):
                action = self.choose_action(state)
                transition = self.env.step(action)
                next_state = transition.next_state
                total_reward += transition.reward

                self.update(state, action, transition.reward, next_state, transition.done)
                state = next_state

                if transition.done:
                    break

            rewards.append(total_reward)

        return rewards
