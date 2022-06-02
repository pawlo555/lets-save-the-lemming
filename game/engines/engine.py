from abc import ABC, abstractmethod

from game.agents.agent import Move
from game.environment import Environment


class Engine(ABC):
    def __init__(self, environment: Environment):
        self.environment: Environment = environment

    def set_environment(self, environment: Environment):
        self.environment = environment

    @abstractmethod
    def change_environment(self, move: Move) -> Environment:
        raise NotImplementedError


class SimpleEngine(Engine):
    def change_environment(self, move: Move) -> Environment:
        if move == Move.LEFT:
            new_position = (self.environment.agent_position[0]-1, self.environment.agent_position[1])
            if new_position[0] > 0:
                self.environment.agent_position = new_position
            return self.environment
        if move == Move.RIGHT:
            new_position = (self.environment.agent_position[0]+1, self.environment.agent_position[1])
            if new_position[0] < len(self.environment.map.elements[0]):
                self.environment.agent_position = new_position
            return self.environment
