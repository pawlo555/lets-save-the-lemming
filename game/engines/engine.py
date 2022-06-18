from abc import ABC, abstractmethod

from game.agents.agent import Move
from game.background import Background
from game.environment import Environment


class Engine(ABC):

    @abstractmethod
    def change_environment(self, move: Move, environment: Environment) -> Environment:
        raise NotImplementedError


class SimpleEngine(Engine):
    def change_environment(self, move: Move, environment: Environment) -> Environment:
        if move == Move.LEFT:
            self.perform_move_left(environment)
        if move == Move.RIGHT:
            self.perform_move_right(environment)
        if environment.map.get_tile_at_position(environment.agent_position) == Background.GRAVITY:
            self.perform_fall(environment)
        if environment.map.get_tile_at_position(environment.agent_position) == Background.HOT_AIR:
            self.perform_hot_air_fly(environment)
        environment.time_to_death -= 1

        return environment

    def perform_move_left(self, environment: Environment):
        new_position = (environment.agent_position[0], environment.agent_position[1] - 1)
        if new_position[1] > 0 and environment.map.get_tile_at_position(new_position) != Background.ROCK:
            environment.agent_position = new_position

    def perform_move_right(self, environment: Environment):
        new_position = (environment.agent_position[0], environment.agent_position[1] + 1)
        if new_position[1] < len(environment.map.elements[0]) and environment.map.get_tile_at_position(new_position) != Background.ROCK:
            environment.agent_position = new_position

    def perform_fall(self, environment: Environment):
        i = environment.agent_position[0]
        j = environment.agent_position[1]
        if i + 1 < len(environment.map.elements):
            if environment.map.elements[i+1][j] != Background.ROCK:
                environment.agent_position = (i + 1, j)

    def perform_hot_air_fly(self, environment: Environment):
        i = environment.agent_position[0]
        j = environment.agent_position[1]
        how_much_up = environment.map.hot_air_values[j]
        new_i = i
        while how_much_up and environment.map.get_tile_at_position((new_i, j)) == Background.HOT_AIR and new_i >= 0:
            new_i -= 1
            how_much_up -= 1
        if environment.map.get_tile_at_position((new_i, j)) == Background.ROCK:
            new_i += 1
        environment.agent_position = (new_i, j)
