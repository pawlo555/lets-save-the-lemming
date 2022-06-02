from game.map import Map
from dataclasses import dataclass


@dataclass
class Environment:
    map: Map
    agent_position: (int, int)
    turn_to_death: int

    def prepare_environment_for_new_agent(self, time_to_death: int):
        self.agent_position = self.map.find_start_position()
        self.turn_to_death = time_to_death
