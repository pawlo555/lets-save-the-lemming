from enum import Enum


class StateType(Enum):
    AGENT_ALIVE = 0
    AGENT_WIN = 1
    AGENT_LOSE_TRAP = 2
    AGENT_LOSE_EXPLODE = 3
