from abc import ABC, abstractmethod
from game.agents.agent import Move
from game.environment import Environment


class Reward(ABC):
    """
    Abstract class representing reward that agent got after each move.
    """
    @abstractmethod
    def get_reward(self, environment: Environment, move: Move, new_environment: Environment) -> int:
        raise NotImplementedError


class SillyReward(Reward):
    def get_reward(self, environment: Environment, move: Move, new_environment: Environment) -> int:
        return 1
