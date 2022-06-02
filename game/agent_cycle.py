from agents.agent import Agent
from environment import Environment
from enum import Enum
from game.rewards.reward import Reward
from game.engines.engine import Engine
from game.background import Background


class StateType(Enum):
    AGENT_ALIVE = 0
    AGENT_WIN = 1
    AGENT_LOSE = 2


class AgentRunner:

    def __init__(self, environment: Environment, agent: Agent, reward: Reward, engine: Engine) -> None:
        self.environment = environment
        self.agent = agent
        self.engine = engine
        self.engine.set_environment(environment)
        self.reward = reward

    def next_state(self) -> StateType:
        move = self.agent.move(self.environment)
        new_environment = self.engine.change_environment(move)
        reward_value = self.reward.get_reward(self.environment, move, new_environment)
        self.agent.update_policy(reward_value)
        self.environment = new_environment
        return self.calc_state_type()

    def calc_state_type(self) -> StateType:
        tile = self.environment.map.get_tile_at_position(self.environment.agent_position)
        if tile == Background.END:
            return StateType.AGENT_WIN
        elif tile == Background.TRAP:
            return StateType.AGENT_LOSE
        else:
            return StateType.AGENT_ALIVE
