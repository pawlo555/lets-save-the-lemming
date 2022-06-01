from abc import ABC, abstractmethod
from enum import Enum
from game.environment import Environment


class Move(Enum):
    UP = 0
    UP_RIGHT = 1
    RIGHT = 2
    DOWN_RIGHT = 3
    DOWN = 4
    DOWN_LEFT = 5
    LEFT = 6
    UP_LEFT = 7


class Agent(ABC):
    @abstractmethod
    def move(self, environment: Environment) -> Move:
        raise NotImplementedError

    @abstractmethod
    def update_policy(self, reward: int) -> None:
        raise NotImplementedError