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
        self.file.write("WIN," + str(time) + "\n")
        print("WIN," + str(time) + "\n")

    def log_lose(self, time):
        self.file.write("LOST," + str(time) + "\n")
        print("LOST," + str(time) + "\n")

    def close_logger(self):
        self.file.close()
