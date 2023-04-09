from enum import Enum
import random


class Cell(Enum):
    PATH = 0
    WALL = 1
    SOLVED = 2


class Labyrinth:
    def __init__(self, width=10, height=10, cell: Cell = Cell.WALL):
        self.width_ = width * 2 + 1
        self.height_ = height * 2 + 1
        self.grid_ = [[cell] * self.width_ for i in range(self.height_)]
        self.solved_ = [[cell] * self.width_ for i in range(self.height_)]
        self.solutions_ = []
        self.start_coord_ = ()
        self.finish_coord_ = ()

    def set_solved_cell(self, y: int, x: int, cell: Cell):
        self.solved_[y][x] = cell

    def set_cell(self, y: int, x: int, cell: Cell):
        self.grid_[y][x] = cell

    def get_cell(self, y: int, x: int) -> Cell:
        return self.grid_[y][x]

    def get_solved_cell(self, y: int, x: int) -> Cell:
        return self.solved_[y][x]

    def cell_check_wall(self, y: int, x: int, wall_flg: bool) -> bool:
        if wall_flg:
            return self.get_cell(y, x) == Cell.WALL
        else:
            return self.get_cell(y, x) != Cell.WALL

    def cell_check_solved_sol(self, y: int, x: int, solved_flg: bool) -> bool:
        if solved_flg:
            return self.get_solved_cell(y, x) == Cell.SOLVED
        else:
            return self.get_cell(y, x) != Cell.SOLVED

    def cell_check_solved_wall(self, y: int, x: int, solved_flg: bool) -> bool:
        if solved_flg:
            return self.get_solved_cell(y, x) == Cell.WALL
        else:
            return self.get_solved_cell(y, x) != Cell.WALL

    def get_random_cell(self) -> tuple:
        return random.randrange(1, self.height_, 2), random.randrange(1, self.width_, 2)

    def neighbour_check(self, row: int, column: int, wall_flg: bool = False) -> list[tuple[int, int]]:
        neighbours = []

        if row > 1 and self.cell_check_wall(row - 2, column, wall_flg):  # if not top border
            neighbours.append((row - 2, column))
        if row < self.height_ - 2 and self.cell_check_wall(row + 2, column, wall_flg):  # if not bottom border
            neighbours.append((row + 2, column))
        if column > 1 and self.cell_check_wall(row, column - 2, wall_flg):  # if not left border
            neighbours.append((row, column - 2))
        if column < self.width_ - 2 and self.cell_check_wall(row, column + 2, wall_flg):  # if not right border
            neighbours.append((row, column + 2))

        random.shuffle(neighbours)
        return neighbours

    def visualize(self):
        for i in range(self.height_):
            for j in range(self.width_):
                if self.cell_check_wall(i, j, True):
                    print(u"\u2588\u2588\u2588", sep='', end='')
                else:
                    print("   ", sep='', end='')
            print('\n', sep='', end='')
