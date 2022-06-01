from game.map import Map
from dataclasses import dataclass


@dataclass
class Environment:
    map: Map
    agent_position: (int, int)
