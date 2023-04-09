from src.Entities.labyrinth import Labyrinth
from src.Entities.labyrinth import Cell
from src.Labyrinth_generation.general_generation_methods import update_cells, add_entrance_finish
import random


def generate_binary_tree(width: int, height: int) -> Labyrinth:
    labyrinth = Labyrinth(width, height, Cell.WALL)

    for y in range(1, labyrinth.height_, 2):
        for x in range(1, labyrinth.width_, 2):
            labyrinth.set_cell(y, x, Cell.PATH)

            y_n, x_n = binary_neighbours(labyrinth, y, x)
            labyrinth.set_cell(y_n, x_n, Cell.PATH)

    add_entrance_finish(labyrinth)
    return labyrinth


def binary_neighbours(labyrinth: Labyrinth, y: int, x: int):
    neighbours = []
    pos = [(1, 0), (0, 1)]
    for dy, dx in pos:
        y_n = y + dy
        x_n = x + dx
        if 0 < y_n < (labyrinth.height_ - 1) and 0 < x_n < (labyrinth.width_ - 1):
            neighbours.append((y_n, x_n))
    if not(len(neighbours) == 0):
        return random.choice(neighbours)
    return y, x

