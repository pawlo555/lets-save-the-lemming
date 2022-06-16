from game.environment import Environment
from game.agents.agent import Agent
from game.reward import Reward
from game.engines.engine import Engine
from game.agent_cycle import AgentRunner
from game.states import StateType
from game.logger import Logger


class ExperimentRunner:
    def __init__(self, environment: Environment, agent: Agent, reward: Reward, engine: Engine, logger: Logger,
                 turn_for_agent: int = 30, episodes: int = 300):
        self.environment: Environment = environment
        self.logger: Logger = logger
        self.turn_for_agent: int = turn_for_agent

        self.environment.prepare_environment_for_new_agent()
        self.agent_runner: AgentRunner = AgentRunner(environment, agent, reward, engine)

        self.episodes = episodes
        self.current_episode = 0

    def next(self):
        state_type = self.agent_runner.next_state()
        if state_type == StateType.AGENT_LOSE_TRAP:
            self.on_lost_trap()
        elif state_type == StateType.AGENT_LOSE_EXPLODE:
            self.on_lost_explode()
        elif state_type == StateType.AGENT_WIN:
            self.on_win()
        else:
            self.on_survive()

    def on_lost_trap(self):
        self.logger.log_lose_trap(self.environment.time_to_death, self.agent_runner.calc_average())
        self.update_episode()
        self.environment.prepare_environment_for_new_agent()

    def on_lost_explode(self):
        self.logger.log_lose_explode(self.environment.time_to_death, self.agent_runner.calc_average())
        self.update_episode()
        self.environment.prepare_environment_for_new_agent()

    def on_win(self):
        self.logger.log_win(self.environment.time_to_death, self.agent_runner.calc_average())
        self.update_episode()
        self.environment.prepare_environment_for_new_agent()

    def on_survive(self):
        pass

    def update_episode(self):
        self.agent_runner.reset_average()
        self.current_episode += 1
        if self.episodes <= self.current_episode:
            raise TimeoutError("Experiment ends")
