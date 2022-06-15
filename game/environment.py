from game.map import Map
from dataclasses import dataclass


@dataclass
class Environment:
    map: Map
    agent_position: (int, int)
    total_time_to_death: int
    time_to_death: int

    def __init__(self, map: Map, agent_position: (int, int), total_time_to_death):
        self.map = map
        self.agent_position = agent_position
        self.total_time_to_death = total_time_to_death

    def prepare_environment_for_new_agent(self):
        self.agent_position = self.map.start_position
        self.time_to_death = self.total_time_to_death
