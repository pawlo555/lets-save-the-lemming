from typing import List

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RESULTS = ["WIN", "LOSE_TRAP", "LOSE_EXPLODE"]


def read_data(path: str):
    df = pd.read_csv(path, header=None, names=["result", "turns", "rewards"])
    return df


def plot_saved_lemming(df_list: List[pd.DataFrame]) -> None:
    pass


def plot_last_lemmings_fate(df_list: List[pd.DataFrame], episodes: int) -> None:
    pass


def plot_last_episodes_time(df_list: List[pd.DataFrame], episodes: int) -> None:
    pass


def plot_average_reward(df_list: List[pd.DataFrame], episodes: int) -> None:
    pass


if __name__ == '__main__':
    logs = []
    for i in range(5):
        logs.append(read_data("log/logs_1.txt"))

    plot_saved_lemming(logs)
    plot_last_lemmings_fate(logs, 20)
    plot_last_episodes_time(logs, 20)
    plot_average_reward(logs, 20)
