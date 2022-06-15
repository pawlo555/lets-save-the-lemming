from abc import ABC, abstractmethod

from game.agents.agent import Move
from game.background import Background
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
            self.perform_move_left()
        if move == Move.RIGHT:
            self.perform_move_right()
        if self.environment.map.get_tile_at_position(self.environment.agent_position) == Background.GRAVITY:
            self.perform_fall()
        if self.environment.map.get_tile_at_position(self.environment.agent_position) == Background.HOT_AIR:
            self.perform_hot_air_fly()
        self.environment.turn_to_death -= 1
        return self.environment

    def perform_move_left(self):
        new_position = (self.environment.agent_position[0], self.environment.agent_position[1] - 1)
        if new_position[1] > 0 and self.environment.map.get_tile_at_position(new_position) != Background.ROCK:
            self.environment.agent_position = new_position

    def perform_move_right(self):
        new_position = (self.environment.agent_position[0], self.environment.agent_position[1] + 1)
        if new_position[1] < len(self.environment.map.elements[0]) and self.environment.map.get_tile_at_position(new_position) != Background.ROCK:
            self.environment.agent_position = new_position

    def perform_fall(self):
        i = self.environment.agent_position[0]
        j = self.environment.agent_position[1]
        if i + 1 < len(self.environment.map.elements):
            if self.environment.map.elements[i+1][j] == Background.GRAVITY:
                self.environment.agent_position = (i + 1, j)

    def perform_hot_air_fly(self):
        i = self.environment.agent_position[0]
        j = self.environment.agent_position[1]
        how_much_up = self.environment.map.hot_air_values[j]
        new_i = i
        while how_much_up and self.environment.map.get_tile_at_position((new_i, j)) == Background.HOT_AIR and new_i > 0:
            new_i -= 1
            how_much_up -= 1
        if self.environment.map.get_tile_at_position((new_i, j)) == Background.ROCK:
            new_i += 1
        self.environment.agent_position = (new_i, j)
