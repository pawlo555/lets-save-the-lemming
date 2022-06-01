from game.tiles_reader import read_tiles_from_file
from game.map import Background


def test_reading_tiles_test():
    output = read_tiles_from_file("tests/test_game/example_map.txt")
    true_output = [[Background.START, Background.GRAVITY, Background.HOT_AIR],
                   [Background.TRAP, Background.ROCK, Background.END]]
    assert output == true_output
