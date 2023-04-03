from Entities.labyrinth import Labyrinth
from Entities.labyrinth import Cell

def generate(width, height) -> Labyrinth:
    path = []

    labyrinth = Labyrinth(width, height, Cell.WALL)
    y, x = labyrinth.get_random_cell()
    labyrinth.set_cell(y, x, Cell.PATH)
    path.append((y, x))

    while path:
        (y, x) = path[-1]
        neighbours = labyrinth.neighbour_check(y, x, True)

    return labyrinth