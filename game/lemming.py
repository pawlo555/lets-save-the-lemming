from enum import Enum


class Moves(Enum):
    LEFT = 0
    RIGHT = 1


class Lemming:
    def __init__(self, start_position):
        self.position = start_position
