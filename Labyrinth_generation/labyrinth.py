from Labyrinth_generation.cell import Cell
import random

class Labyrinth:
    def __init__(self, width, height, cell: Cell = Cell.WALL ):
        self.width_ = width * 2 + 1
        self.height_ = height * 2 + 1
        self.grid_ = [[cell] * self.width_] * self.height_
        self.solutions_ = []

    def set_cell(self, y, x, cell: Cell):
        self.grid_[y][x] = cell

    def get_cell(self, y, x) -> Cell:
        return self.grid_[y][x]

    def cell_check(self, y, x, wall_flg):
        if wall_flg:
            return self.get_cell(y, x) == Cell.WALL
        else:
            return self.get_cell(y, x) != Cell.WALL


    def neighbour_check(self, row, column, wall_flg: bool = False) -> list[tuple[int, int]]:
        neighbours = []

        if row > 1 and self.cell_check(row - 2, column, wall_flg): #if not left border
            neighbours.append((row - 2, column))
        if


        random.shuffle(neighbours)
        return neighbours


