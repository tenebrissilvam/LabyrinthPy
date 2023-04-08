from src.Entities.labyrinth import Labyrinth
from src.Entities.labyrinth import Cell
from src.Labyrinth_generation.general_generation_methods import update_cells, add_entrance_finish
import random


def generate_dfs(width, height) -> Labyrinth:
    path = []  # list of chosen adjacent cells starting from randomly chosen first cell

    labyrinth = Labyrinth(width, height, Cell.WALL)  # init labyrinth full of walls
    y, x = labyrinth.get_random_cell()  # randomly choose starting cell
    update_cells(labyrinth, y, x, Cell.PATH, path)  # set starting cell as PATH cell
    # labyrinth.set_cell(y, x, Cell.PATH)
    # path.append((y, x))

    while path:
        (y, x) = path[-1]  # continue from last added cell
        neighbours = labyrinth.neighbour_check(y, x, True)
        if not (len(neighbours) == 0):  # if last cell has available adjacent cells
            random.shuffle(neighbours)
            yn, xn = neighbours[0]  # choose first from available
            update_cells(labyrinth, yn, xn, Cell.PATH, path)  # set it as PATH cell
            update_cells(labyrinth, (y + yn) // 2, (x + xn) // 2, Cell.PATH)  # set cell that connects them as PATH
        else:  # if last cell didn't have any available adjacent cells return to previous
            path = path[:-1]
            random.shuffle(path)

    add_entrance_finish(labyrinth)

    return labyrinth
