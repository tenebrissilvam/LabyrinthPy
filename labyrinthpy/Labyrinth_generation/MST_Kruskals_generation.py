from labyrinthpy.Entities.labyrinth import Labyrinth
from labyrinthpy.Entities.labyrinth import Cell
from labyrinthpy.Labyrinth_generation.general_generation_methods import update_cells
import random


def generate_mst_kruskals(width, height) -> Labyrinth:
    labyrinth = Labyrinth(width, height, Cell.WALL)

    return labyrinth