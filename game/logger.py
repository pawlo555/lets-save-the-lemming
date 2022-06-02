from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log_win(self, time):
        raise NotImplementedError

    @abstractmethod
    def log_lose(self, time):
        raise NotImplementedError


class FileLogger(Logger):
    def __init__(self, path):
        self.file = open(path, "w")

    def log_win(self, time):
        self.file.write("WIN,time")

    def log_lose(self, time):
        self.file.write("LOST, time")

    def close_logger(self):
        self.file.close()
