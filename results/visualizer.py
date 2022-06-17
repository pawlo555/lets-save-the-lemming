from typing import List

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RESULTS = ["WIN", "LOSE_TRAP", "LOSE_EXPLODE"]
EXPERIMENTS = 10
TURN_PER_EPISODE = 100


def read_data(path: str):
    df = pd.read_csv(path, header=None, names=["result", "turns", "reward"])
    return df


def plot_saved_lemming(df_list: List[pd.DataFrame]) -> None:
    saved_lemming = np.zeros(df_list[0].shape[0])
    for df in df_list:
        saved_lemming += (df["result"] == "WIN").to_numpy().astype(int)
    fig, ax = plt.subplots()
    for i in range(1, saved_lemming.shape[0]):
        saved_lemming[i] += saved_lemming[i-1]
    saved_lemming /= EXPERIMENTS
    ax.plot(saved_lemming)
    ax.set_ylabel("Average saved lemmings")
    ax.set_xlabel("Episode")
    ax.set_title("Average number of saved lemmings number at selected episode")
    plt.show()


def plot_last_lemmings_fate(df_list: List[pd.DataFrame], episodes: int) -> None:
    total_values = None
    for df in df_list:
        df_last = df.iloc[-episodes:]
        if total_values is None:
            total_values = df_last["result"].value_counts()
        else:
            total_values += df_last["result"].value_counts()
    fig, ax = plt.subplots()
    total_values.keys()
    ax.bar(total_values.keys(), total_values.values, width=1, edgecolor="white", linewidth=0.7)
    ax.set_ylabel("Games with result")
    ax.set_xlabel("Game result")
    ax.set_title("Games results")
    plt.show()


def plot_last_episodes_time(df_list: List[pd.DataFrame], episodes: int) -> None:
    times = np.zeros((EXPERIMENTS, episodes))
    for i, df in enumerate(df_list):
        df_last = df.iloc[-episodes:]
        times[i] = TURN_PER_EPISODE - df_last["turns"].to_numpy().astype(int)
    fig, ax = plt.subplots()
    hist = times.reshape(EXPERIMENTS*episodes)
    ax.hist(hist)
    ax.set_ylabel("Number of episodes")
    ax.set_xlabel("Number of time in episode")
    ax.set_title("Histogram of episode time")
    plt.show()


def plot_average_reward(df_list: List[pd.DataFrame], episodes: int) -> None:
    rewards = np.zeros((EXPERIMENTS, episodes))
    for i, df in enumerate(df_list):
        df_last = df.iloc[-episodes:]
        rewards[i] = df_last["reward"].to_numpy().astype(int)
    fig, ax = plt.subplots()
    rewards = np.average(rewards, axis=-1)
    ax.bar(range(10), rewards)
    ax.set_ylabel("Average reward")
    ax.set_xlabel("Experiment number")
    ax.set_title("Average reward at experiment")
    plt.show()


if __name__ == '__main__':
    logs = []
    for i in range(1, EXPERIMENTS + 1):
        path = f"log/logs_{i}.txt"
        logs.append(read_data(path))
    plt.rcParams['figure.figsize'] = [13, 8]
    plot_saved_lemming(logs)
    plot_last_lemmings_fate(logs, 20)
    plot_last_episodes_time(logs, 20)
    plot_average_reward(logs, 20)
