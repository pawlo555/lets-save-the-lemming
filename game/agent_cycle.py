from agents.agent import Agent
from environment import Environment

from game.reward import Reward
from game.states import StateType
from game.engines.engine import Engine
from game.background import Background


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
        new_state = self.calc_state_type(new_environment)
        reward_value = self.reward.get_reward(self.environment, move, new_environment, new_state)
        self.agent.update_policy(reward_value, move, new_environment, self.environment)
        self.environment = new_environment
        return self.calc_state_type(new_environment)

    def calc_state_type(self, environment: Environment) -> StateType:
        tile = environment.map.get_tile_at_position(environment.agent_position)
        if tile == Background.END or environment.turn_to_death == 0:
            return StateType.AGENT_WIN
        elif tile == Background.TRAP:
            return StateType.AGENT_LOSE
        else:
            return StateType.AGENT_ALIVE
