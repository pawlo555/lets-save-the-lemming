import time
from typing import Dict

import pygame
import os

from game.map import Map
from game.tiles_reader import read_tiles_from_file
from game.background import Background
from game.experiment_runner import ExperimentRunner
from game.environment import Environment
from game.agents.lemming import RandomLemming
from game.reward import SillyReward
from game.logger import FileLogger
from game.engines.engine import SimpleEngine

SQUARE_SIZE = 40


def main():
    pygame.init()
    tiles = read_tiles_from_file("resources/map.txt")
    game_map = Map(tiles, hot_air_values=[0, 2, 0, 0, 0, 5, 0, 0])
    size = game_map.get_size()

    turn_per_agent = 30
    environment = Environment(game_map, game_map.start_position, turn_per_agent)
    experiment_runner = ExperimentRunner(environment, RandomLemming(), SillyReward(), SimpleEngine(environment),
                                         FileLogger("logs.txt"))

    screen: pygame.Surface = pygame.display.set_mode(size)

    images = load_images()
    lemming_image = pygame.image.load(os.path.join('resources', 'lemming.png'))
    display_map(screen, images, environment, lemming_image)

    # infinite loop
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        experiment_runner.next()
        time.sleep(0.05)
        print(experiment_runner.environment.agent_position)
        display_map(screen, images, environment, lemming_image)
        pygame.display.update()


def load_images() -> Dict[Background, pygame.Surface]:
    return {
        Background.ROCK: pygame.image.load(os.path.join('resources', 'rock.png')),
        Background.TRAP: pygame.image.load(os.path.join('resources', 'trap.png')),
        Background.START: pygame.image.load(os.path.join('resources', 'start.png')),
        Background.END: pygame.image.load(os.path.join('resources', 'exit.png')),
        Background.HOT_AIR: pygame.image.load(os.path.join('resources', 'air_up.png')),
        Background.GRAVITY: pygame.image.load(os.path.join('resources', 'background.png'))
    }


def display_tile(screen: pygame.Surface, images: Dict[Background, pygame.Surface], element: Background, X: int,
                 Y: int) -> None:
    if element == Background.TRAP:
        screen.blit(images[Background.GRAVITY], (X, Y))
    screen.blit(images[element], (X, Y))


def display_map(screen: pygame.Surface, images: Dict[Background, pygame.Surface], environment: Environment,
                lemming_image: pygame.Surface) -> None:
    for i, row in enumerate(environment.map.elements):
        for j, element in enumerate(row):
            display_tile(screen, images, element, j*SQUARE_SIZE, i*SQUARE_SIZE)
    screen.blit(lemming_image, (environment.agent_position[1]*SQUARE_SIZE, environment.agent_position[0]*SQUARE_SIZE))


if __name__ == '__main__':
    main()
