from game.map import Map
from dataclasses import dataclass


@dataclass
class Environment:
    map: Map
    agent_position: (int, int)
    turn_to_death: int
    time_to_death: int

    def prepare_environment_for_new_agent(self, time_to_death: int):
        self.agent_position = self.map.start_position
        self.turn_to_death = time_to_death
        self.time_to_death = time_to_death

    def __init__(self, map: Map, agent_position: (int, int), time_to_death):
        self.map = map
        self.agent_position = agent_position
        self.time_to_death = time_to_death
