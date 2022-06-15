from typing import List, Optional

from game.background import Background


class Map:
    SQUARE_SIZE = 40

    def __init__(self, elements: List[List[Background]], hot_air_values: Optional[List[int]] = None):
        """
        :param elements: List of background elements, elements[i] refer to i row
        :param hot_air_values: Value for hot air in each column
        """
        for i in range(1, len(elements)):
            assert len(elements[0]) == len(elements[i]), "Map must be a square"
        self.elements: List[List[Background]] = elements
        self.hot_air_values: List[int] = [1 for _ in range(len(elements[0]))]
        if hot_air_values is not None:
            assert len(hot_air_values) == len(self.hot_air_values), "hot_air_values list has wrong size"
            self.hot_air_values = hot_air_values
        self.start_position = self.find_position(Background.START)
        self.end_position = self.find_position(Background.END)

    def find_position(self, element_name: Background) -> (int, int):
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                if self.elements[i][j] == element_name:
                    return i, j
        raise RuntimeError("Map doesnt have ", element_name)

    def get_size(self) -> (int, int):
        return len(self.elements[0])*self.SQUARE_SIZE, len(self.elements)*self.SQUARE_SIZE

    def get_tile_at_position(self, position):
        return self.elements[position[0]][position[1]]
