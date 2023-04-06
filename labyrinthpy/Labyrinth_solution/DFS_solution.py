import random
import copy
from labyrinthpy.Entities.labyrinth import Labyrinth
from labyrinthpy.Entities.labyrinth import Cell


def solve(labyrinth):
    solution_path = [(1, labyrinth.start_coord_[1])]
    cnt = 0
    while not near_target(labyrinth, solution_path[-1], labyrinth.finish_coord_):
        free_ngh = get_free_neighbours(labyrinth, solution_path[-1])
        random.shuffle(free_ngh)
        cnt += 1
        if len(free_ngh) > 1 and len(solution_path) > 2:
            if solution_path[-3] in free_ngh:
                free_ngh.remove(solution_path[-3])
        cell_r = random.choice(free_ngh)
        solution_path.append(((solution_path[-1][0] + cell_r[0]) // 2, (solution_path[-1][1] + cell_r[1]) // 2))
        solution_path.append(cell_r)
    return solution_path


def get_free_neighbours(labyrinth, cell):
    y, x = cell
    free_ngh = []

    if (y > 1 and not (labyrinth.get_cell(y - 1, x) == Cell.WALL)
            and not (labyrinth.get_cell(y - 2, x) == Cell.WALL)):
        free_ngh.append((y - 2, x))
    if (y < labyrinth.height_ - 2
            and not (labyrinth.get_cell(y + 1, x) == Cell.WALL)
            and not (labyrinth.get_cell(y + 2, x) == Cell.WALL)):
        free_ngh.append((y + 2, x))
    if (x > 1 and not (labyrinth.get_cell(y, x - 1) == Cell.WALL)
            and not (labyrinth.get_cell(y, x - 2) == Cell.WALL)):
        free_ngh.append((y, x - 2))
    if (x < labyrinth.width_ - 2
            and not (labyrinth.get_cell(y, x + 1) == Cell.WALL)
            and not (labyrinth.get_cell(y, x + 2) == Cell.WALL)):
        free_ngh.append((y, x + 2))
    return free_ngh


def cleanup_dead_ends(labyrinth, solution_path):
    found_flg = True
    attempts = 0
    attempts_threshold = len(solution_path)

    while found_flg and len(solution_path) > 2 and attempts < attempts_threshold:
        found_flg = False
        attempts += 1
        i_f = 0
        i_l = 0

        for i in range(len(solution_path) - 1):
            f = solution_path[i]
            if f in solution_path[i + 1:]:
                i_f = i
                i_l = solution_path[i + 1:].index(f) + i + 1
                found_flg = True
                break

            if found_flg:
                solution_path = solution_path[:i_f] + solution_path[i_l:]

        if len(solution_path) > 1:
            if solution_path[0] == labyrinth.start_coord_:
                solution_path = solution_path[1:]
            if solution_path[-1] == labyrinth.finish_coord_:
                solution_path = solution_path[:-1]
        return solution_path


def near_target(labyrinth, cell, target):
    if not cell or not target:
        return False
    return ((cell[0] == target[0] and abs(cell[1] - target[1]) < 2) or
            (cell[1] == target[1] and abs(cell[0] - target[0]) < 2))


def show_solution(labyrinth):
    labyrinth.solved_ = copy.deepcopy(labyrinth.grid_)
    labyrinth.solutions_ = solve(labyrinth)
    for c in labyrinth.solutions_:
        labyrinth.set_solved_cell(c[0], c[1], Cell.SOLVED)
