import random

from src.Entities.labyrinth import Cell, Labyrinth
from src.Labyrinth_generation.general_generation_methods import update_cells, add_entrance_finish


def generate_mst_prims(width: int, height: int) -> Labyrinth:
    labyrinth = Labyrinth(width, height, Cell.WALL)
    y, x = labyrinth.get_random_cell()  # randomly choose starting cell
    update_cells(labyrinth, y, x, Cell.PATH)

    neighbours = labyrinth.neighbour_check(y, x, True)

    while len(neighbours) >= 1:
        rand = random.randrange(len(neighbours))
        y_r, x_r = neighbours[rand]
        update_cells(labyrinth, y_r, x_r, Cell.PATH)
        neighbours = neighbours[:rand] + neighbours[rand + 1:]
        new_neighbours = labyrinth.neighbour_check(y_r, x_r)
        near_y_r, near_x_r = new_neighbours[0]
        update_cells(labyrinth, (y_r + near_y_r) // 2, (x_r + near_x_r) // 2, Cell.PATH)

        unvisited = labyrinth.neighbour_check(y_r, x_r, True)
        neighbours = list(set(neighbours + unvisited))

    add_entrance_finish(labyrinth)

    return labyrinth
