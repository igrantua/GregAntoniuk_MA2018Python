"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    line_length = len(line)
    result_list = [0] * line_length
    result_index = 0

    for line_index in range(line_length):
        if line[line_index] != 0:
            result_list[result_index] = line[line_index]
            result_index += 1

    for index in range(line_length-1):
        if result_list[index] == result_list[index+1]:
            result_list[index] = result_list[index] * 2
            result_list.pop(index + 1)
            result_list.append(0)

    return result_list


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, _grid_height, _grid_width):
        self._grid_height = _grid_height
        self._grid_width = _grid_width
        self.reset()
        self._init_tiles = {UP: [[0, j] for j in range(self._grid_width)],
                            DOWN: [[self._grid_height - 1, j] for j in range(self._grid_width)],
                            LEFT: [[i, 0] for i in range(self._grid_height)],
                            RIGHT: [[i, self._grid_width - 1] for i in range(self._grid_height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                      for dummy_row in range(self._grid_height)]

        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        tile_changed = False

        # set appropriate number of steps in loop
        if direction is LEFT or direction is RIGHT:
                steps = self._grid_width
        elif direction is UP or direction is DOWN:
                steps = self._grid_height

        for start_tile in self._init_tiles[direction]:

            tile_values = []
            tile_indices = []

            # create a list of row/column for merge
            for step in range(steps):
                row = start_tile[0] + step * OFFSETS[direction][0]
                col = start_tile[1] + step * OFFSETS[direction][1]
                tile_indices.append((row, col))

            # get values in row/column
            for (dummy_row, dummy_col) in tile_indices:
                tile_values.append(self.get_tile(dummy_row, dummy_col))

            merged = merge(tile_values)
            if tile_values != merged:
                tile_changed = True

            # change values in grid
            for dummy_tile in range(len(merged)):
                self._grid[tile_indices[dummy_tile][0]][tile_indices[dummy_tile][1]] = merged[dummy_tile]

        if tile_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # create list of empty cells
        empty_cells = []
        for col in range(self._grid_width):
            for row in range(self._grid_height):
                if self._grid[row][col] == 0:
                    empty_cells.append([row, col])

        # create new tile
        if len(empty_cells) > 0:
            tile = random.choice([2] * 9 + [4])
            empty = random.choice(empty_cells)
            self._grid[empty[0]][empty[1]] = tile

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

