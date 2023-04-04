from labyrinthpy.Entities.labyrinth import Labyrinth
from labyrinthpy.Entities.labyrinth import Cell
from labyrinthpy.Labyrinth_generation.general_generation_methods import update_cells
import random

def generate_mst_prims(width, height) -> Labyrinth:

    labyrinth = Labyrinth(width, height, Cell.WALL)
    y, x = labyrinth.get_random_cell() #randomly choose starting cell
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

    for i in range(1, labyrinth.width_): #add entrance
        if labyrinth.cell_check(1, i, False):
            labyrinth.set_cell(0, i, Cell.PATH)
            #labyrinth.start_coord_ = (0, i)
            break

    for i in range(labyrinth.width_ - 2, 1, -1): #add exit
        if labyrinth.cell_check(labyrinth.height_ - 2, i, False):
            labyrinth.set_cell(labyrinth.height_ - 1, i, Cell.PATH)
            #labyrinth.finish_coord_ = (labyrinth.height_ - 1, i)
            break

    return labyrinth