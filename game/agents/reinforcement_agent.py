import numpy as np

from math import inf
from typing import List, Tuple, Optional
from game.agents.agent import Agent, Move
from game.environment import Environment
import random


class ReinforcementAgent(Agent):
    def __init__(self, actions: List[Move], size: Tuple[int], alpha: float, discount_factor: float, epsilon: float):
        self.alpha = alpha
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.actions = actions
        self.Q = {}
        for action in actions:
            self.Q[action] = np.zeros(size)

    def move(self, environment: Environment) -> Move:
        rand = random.random()
        if rand < self.epsilon:
            return self.random_move()
        else:
            move, _ = self.find_best_move(environment.agent_position)
            print("Move: ", move)
            return move

    def update_policy(self, reward: int, move: Move, prev_env: Environment, new_env: Environment) -> None:
        #print(reward, move)
        pos = prev_env.agent_position
        _, expected_reward = self.find_best_move(new_env.agent_position)
        prev_q_value = self.Q[move][pos[0], pos[1]]
        #print(pos, self.Q[move][pos[0], pos[1]])
        self.Q[move][pos[0], pos[1]] += self.alpha * (reward + self.discount_factor*expected_reward - prev_q_value)
        #print("QQQ", pos, self.Q[move][pos[0], pos[1]])

    def random_move(self) -> Move:
        return random.choice(self.actions)

    def find_best_move(self, position: Tuple[int]) -> (Move, float):
        best_action: Optional[Move] = None
        best_value = -inf
        for action in self.actions:
            move_value = self.Q[action][position[0], position[1]]
            #print(action, move_value)
            if move_value > best_value:
                best_action = action
                best_value = move_value
        #print(best_action, best_value)
        return best_action, best_value
