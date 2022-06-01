import random

from game.agents.agent import Agent, Move
from game.environment import Environment


class RandomLemming(Agent):
    def update_policy(self, reward: int) -> None:
        pass

    def move(self, environment: Environment) -> Move:
        if random.random() > 0.5:
            return Move.LEFT
        else:
            return Move.RIGHT
