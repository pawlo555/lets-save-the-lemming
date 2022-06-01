from abc import ABC, abstractmethod
from typing import Optional

from game.agents.agent import Move
from game.environment import Environment


class Engine(ABC):
    def __init__(self):
        self.environment: Optional[Environment] = None

    def set_environment(self, environment: Environment):
        self.environment = environment

    @abstractmethod
    def change_environment(self, move: Move) -> Environment:
        raise NotImplementedError
