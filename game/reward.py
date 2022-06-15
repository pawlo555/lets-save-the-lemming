from abc import ABC, abstractmethod

from game.states import StateType
from game.agents.agent import Move
from game.environment import Environment
from game.map import Map


class Reward(ABC):
    """
    Abstract class representing reward that agent got after each move.
    """
    @abstractmethod
    def get_reward(self, environment: Environment, move: Move, new_environment: Environment, state: StateType) -> int:
        raise NotImplementedError


class SillyReward(Reward):
    def get_reward(self, environment: Environment, move: Move, new_environment: Environment, state: StateType) -> int:
        return 1


class NormalReward(Reward):
    def get_reward(self, environment: Environment, move: Move, new_environment: Environment, state: StateType) -> int:
        state_reward = self.calc_state_reward(state)
        print("Comp", new_environment.agent_position, environment.agent_position)
        turn_penalty = environment.time_to_death - environment.total_time_to_death
        difference = self.calc_distance(environment.agent_position, environment.map) - self.calc_distance(new_environment.agent_position, new_environment.map)
        print("Reward:", state_reward, turn_penalty, difference)
        return turn_penalty + difference + state_reward

    def calc_distance(self, position: (int, int), map: Map):
        end_position = map.end_position
        return abs(end_position[0] - position[0]) + abs(end_position[1] - position[1])

    def calc_state_reward(self, state: StateType) -> int:
        if state == StateType.AGENT_WIN:
            return 100
        elif state == StateType.AGENT_LOSE:
            return -100
        else:
            return 0
