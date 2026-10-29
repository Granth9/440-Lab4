from vacuum_env import VacuumEnvironment
from q_learning import QLearningAgent


env = VacuumEnvironment()
agent = QLearningAgent(env=env, alpha=0.1, gamma=0.9, epsilon=0.1)
print(env.render())
print(agent.train(episodes=5, max_steps_per_episode=10))
