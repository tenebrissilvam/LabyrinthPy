from src.Entities.labyrinth import Labyrinth
from src.Entities.labyrinth import Cell
from src.Labyrinth_generation.general_generation_methods import update_cells, add_entrance_finish
import random


def generate_mst_kruskals(width: int, height: int) -> Labyrinth:
    labyrinth = Labyrinth(width, height, Cell.WALL)
    vertices = []
    for y in range(1, labyrinth.height_ - 1, 2):
        for x in range(1, labyrinth.width_ - 1, 2):
            vertices.append([(y, x)])
            labyrinth.set_cell(y, x, Cell.PATH)
    edges = []
    for y in range(2, labyrinth.height_ - 1, 2):
        for x in range(1, labyrinth.width_ - 1, 2):
            edges.append((y, x))
    for y in range(1, labyrinth.height_ - 1, 2):
        for x in range(2, labyrinth.width_ - 1, 2):
            edges.append((y, x))
    random.shuffle(edges)
    while len(vertices) > 1:
        y_0, x_0 = edges[0]
        edges = edges[1:]
        vert1 = -1
        vert2 = -1
        if y_0 % 2 == 0:
            vert1 = sum([i if (y_0 - 1, x_0) in j else 0 for i, j in enumerate(vertices)])
            vert2 = sum([i if (y_0 + 1, x_0) in j else 0 for i, j in enumerate(vertices)])
        else:
            vert1 = sum([i if (y_0, x_0 - 1) in j else 0 for i, j in enumerate(vertices)])
            vert2 = sum([i if (y_0, x_0 + 1) in j else 0 for i, j in enumerate(vertices)])

        if vert1 != vert2:
            vert3 = vertices[vert1] + vertices[vert2]

            vert1_rm = list(vertices[vert1])
            vert2_rm = list(vertices[vert2])

            vertices = [v for v in vertices if v != vert1_rm]
            vertices = [v for v in vertices if v != vert2_rm]

            vertices.append(vert3)
            labyrinth.set_cell(y_0, x_0, Cell.PATH)

    add_entrance_finish(labyrinth)
    return labyrinth


def impossible_waffle(width: int, height: int) -> Labyrinth:
    labyrinth = Labyrinth(width, height, Cell.WALL)
    vertices = []
    for y in range(1, labyrinth.height_ - 1, 2):
        for x in range(1, labyrinth.width_ - 1, 2):
            vertices.append([(y, x)])
            labyrinth.set_cell(y, x, Cell.PATH)

    add_entrance_finish(labyrinth)
    return labyrinth
