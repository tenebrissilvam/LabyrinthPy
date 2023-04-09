import random

from src.Entities.labyrinth import Cell, Labyrinth
from src.Labyrinth_generation.general_generation_methods import add_entrance_finish


def generate_binary_tree(width: int, height: int) -> Labyrinth:
    labyrinth = Labyrinth(width, height, Cell.WALL)

    for y in range(1, labyrinth.height_, 2):
        for x in range(1, labyrinth.width_, 2):
            labyrinth.set_cell(y, x, Cell.PATH) #set current as path

            y_n, x_n = binary_neighbours(labyrinth, y, x)
            labyrinth.set_cell(y_n, x_n, Cell.PATH) #set neighbour as path

    add_entrance_finish(labyrinth)
    return labyrinth


def binary_neighbours(labyrinth: Labyrinth, y: int, x: int):
    neighbours = []
    pos = [(1, 0), (0, 1)]  # choose down or right cell to continue path
    for dy, dx in pos:
        y_n = y + dy
        x_n = x + dx
        if 0 < y_n < (labyrinth.height_ - 1) and 0 < x_n < (labyrinth.width_ - 1):
            neighbours.append((y_n, x_n))
    if not (len(neighbours) == 0):
        return random.choice(neighbours)
    return y, x
