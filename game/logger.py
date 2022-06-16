from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log_win(self, time, average_reward):
        raise NotImplementedError

    @abstractmethod
    def log_lose_trap(self, time, average_reward):
        raise NotImplementedError

    def log_lose_explode(self, time, average_reward):
        raise NotImplementedError


class FileLogger(Logger):
    def __init__(self, path):
        self.file = open(path, "w")

    def log_win(self, time, average_reward):
        self.file.write("WIN," + str(time) + "," + str(average_reward) + "\n")
        print("WIN,", time, average_reward)

    def log_lose_trap(self, time, average_reward):
        self.file.write("LOSE_TRAP," + str(time) + "," + str(average_reward) + "\n")
        print("LOSE_TRAP,", time, average_reward)

    def log_lose_explode(self, time, average_reward):
        self.file.write("LOSE_EXPLODE," + str(time) + "," + str(average_reward) + "\n")
        print("LOSE_EXPLODE,", time, average_reward)

    def close_logger(self):
        self.file.close()
