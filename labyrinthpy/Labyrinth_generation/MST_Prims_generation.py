from labyrinthpy.Entities.labyrinth import Labyrinth
from labyrinthpy.Entities.labyrinth import Cell
from labyrinthpy.Labyrinth_generation.general_generation_methods import update_cells
import random

def generate_dfs(width, height) -> Labyrinth:
    path = [] #list of chosen adjacent cells starting from randomly chosen first cell

    labyrinth = Labyrinth(width, height, Cell.WALL) #init labyrinth full of walls
    y, x = labyrinth.get_random_cell() #randomly choose starting cell
    update_cells(labyrinth, y, x, Cell.PATH, path) #set starting cell as PATH cell
    #labyrinth.set_cell(y, x, Cell.PATH)
    #path.append((y, x))

    while path:
        (y, x) = path[-1] #continue from last added cell
        neighbours = labyrinth.neighbour_check(y, x, True)
        if not(len(neighbours) == 0): #if last cell has available adjacent cells
            random.shuffle(neighbours)
            yn, xn = neighbours[0] #choose first from available
            update_cells(labyrinth, yn, xn, Cell.PATH, path) #set it as PATH cell
            update_cells(labyrinth, (y + yn) // 2, (x + xn) // 2, Cell.PATH) #set cell that connects them as PATH
        else: #if last cell didn't have any available adjacent cells return to previous
            path = path[:-1]
            random.shuffle(path)

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

def generate_mst_prims(width, height) -> Labyrinth:

    labyrinth = Labyrinth(width, height, Cell.WALL)
    y, x = labyrinth.get_random_cell() #randomly choose starting cell
    update_cells(labyrinth, y, x, Cell.PATH)

    neighbours = labyrinth.neighbour_check(y, x)
    return labyrinth