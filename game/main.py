from typing import Dict

import pygame
import os

from game.map import Map
from game.tiles_reader import read_tiles_from_file
from game.background import Background


def main():
    pygame.init()
    tiles = read_tiles_from_file("resources/map.txt")

    game_map = Map(tiles)
    size = game_map.get_size()

    screen: pygame.Surface = pygame.display.set_mode(size)

    images = load_images()

    for i, row in enumerate(game_map.elements):
        for j, element in enumerate(row):
            display_tile(screen, images, element, j*game_map.SQUARE_SIZE, i*game_map.SQUARE_SIZE)
    # infinite loop
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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


def display_tile(screen: pygame.Surface, images: Dict[Background, pygame.Surface], element: Background, X: int, Y: int) -> None:
    if element == Background.TRAP:
        screen.blit(images[Background.GRAVITY], (X, Y))
    screen.blit(images[element], (X, Y))


if __name__ == '__main__':
    main()
