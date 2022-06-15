from game.environment import Environment
from game.agents.agent import Agent
from game.reward import Reward
from game.engines.engine import Engine
from game.agent_cycle import AgentRunner
from game.states import StateType
from game.logger import Logger


class ExperimentRunner:
    def __init__(self, environment: Environment, agent: Agent, reward: Reward, engine: Engine, logger: Logger,
                 turn_for_agent: int = 30):
        self.environment: Environment = environment
        self.logger: Logger = logger
        self.turn_for_agent: int = turn_for_agent

        self.environment.prepare_environment_for_new_agent(self.turn_for_agent)
        self.agent_runner: AgentRunner = AgentRunner(environment, agent, reward, engine)

    def next(self):
        state_type = self.agent_runner.next_state()
        if state_type == StateType.AGENT_LOSE:
            self.on_lost()
        elif state_type == StateType.AGENT_WIN:
            self.on_win()
        else:
            self.on_survive()

    def on_lost(self):
        self.logger.log_lose(self.turn_for_agent-self.environment.turn_to_death)
        self.environment.prepare_environment_for_new_agent(self.turn_for_agent)

    def on_win(self):
        self.logger.log_win(self.turn_for_agent-self.environment.turn_to_death)
        self.environment.prepare_environment_for_new_agent(self.turn_for_agent)

    def on_survive(self):
        pass
