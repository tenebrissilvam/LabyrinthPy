import random

from src.Entities.labyrinth import Cell, Labyrinth
from src.Labyrinth_generation.general_generation_methods import add_entrance_finish


def generate_wilsons(width: int, height: int) -> Labyrinth:
    labyrinth = Labyrinth(width, height, Cell.WALL)
    y, x = labyrinth.get_random_cell()
    labyrinth.set_cell(y, x, Cell.PATH)
    visited_cnt = 1
    y, x = next_cell(labyrinth, visited_cnt)

    while not (y == -1) and not (x == -1):
        solution_path = get_wilsons_path(labyrinth, y, x)
        visited_cnt += solve_wilsons_path(labyrinth, solution_path, y, x)
        y, x = next_cell(labyrinth, visited_cnt)

    add_entrance_finish(labyrinth)
    return labyrinth


def next_cell(labyrinth: Labyrinth, cnt: int) -> (int, int):
    (y, x) = (1, -1)
    found_flg = False

    while not found_flg:
        (y, x) = (y, x + 2)
        if x > labyrinth.width_ - 2:
            (y, x) = (y + 2, 1)
            if y > labyrinth.height_ - 2:
                return -1, -1
        if not (labyrinth.get_cell(y, x) == Cell.PATH):
            found_flg = True
    return y, x


def get_wilsons_path(labyrinth: Labyrinth, y: int, x: int):
    dir_side = get_neighbours(labyrinth, y, x)
    solution_path = {(y, x): dir_side}
    cur_y, cur_x = y + dir_side[0], x + dir_side[1]

    while labyrinth.get_cell(cur_y, cur_x) == Cell.WALL:
        dir_side = get_neighbours(labyrinth, cur_y, cur_x)
        solution_path[(cur_y, cur_x)] = dir_side
        cur_y, cur_x = cur_y + dir_side[0], cur_x + dir_side[1]

    return solution_path


def get_neighbours(labyrinth: Labyrinth, y: int, x: int) -> (int, int):
    neighbours = []
    if y > 1:
        neighbours.append((-2, 0))
    if y < (labyrinth.height_ - 2):
        neighbours.append((2, 0))
    if x > 1:
        neighbours.append((0, -2))
    if x < (labyrinth.width_ - 2):
        neighbours.append((0, 2))

    return random.choice(neighbours)


def solve_wilsons_path(labyrinth: Labyrinth, solution_path, y: int, x: int):
    visit_cnt = 0
    cur_y, cur_x = y, x

    while not(labyrinth.get_cell(cur_y, cur_x) == Cell.PATH):
        labyrinth.set_cell(cur_y, cur_x, Cell.PATH)
        y_n, x_n = cur_y + solution_path[(cur_y, cur_x)][0], cur_x + solution_path[(cur_y, cur_x)][1]
        labyrinth.set_cell((y_n + cur_y) // 2, (x_n + cur_x) // 2, Cell.PATH)
        cur_y, cur_x = y_n, x_n
        visit_cnt += 1
    return visit_cnt
