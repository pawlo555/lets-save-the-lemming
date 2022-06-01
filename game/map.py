from typing import List, Optional

from game.background import Background


class Map:
    SQUARE_SIZE = 40

    def __init__(self, elements: List[List[Background]], hot_air_values: Optional[List[int]] = None):
        """
        :param elements: List of background elements, elements[i] refer to i row
        :param hot_air_values: Value for hot air in each column
        """
        print(elements)
        for i in range(1, len(elements)):
            print(i, len(elements[i]))
            assert len(elements[0]) == len(elements[i]), "Map must be a square"
        self.elements: List[List[Background]] = elements
        self.hot_air_values: List[int] = [1 for _ in range(len(elements[0]))]
        if hot_air_values is not None:
            assert len(hot_air_values) == len(self.hot_air_values), "hot_air_values list has wrong size"
            self.hot_air_values = hot_air_values

    def find_start_position(self) -> (int, int):
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                if self.elements[i][j] == Background.START:
                    return i, j
        raise RuntimeError("Map doesnt have a start point")

    def get_size(self) -> (int, int):
        return len(self.elements[0])*self.SQUARE_SIZE, len(self.elements)*self.SQUARE_SIZE
