from typing import List

from game.background import Background


def read_tiles_from_file(path) -> List[List[Background]]:
    tiles = []
    with open(file=path, mode="r") as f:
        lines = f.readlines()
    for line in lines:
        tiles.append([])
        for element in line[:-1]:
            tiles[-1].append(Background(element))
    return tiles
