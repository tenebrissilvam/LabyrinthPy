from src.Entities.labyrinth import Cell, Labyrinth


def update_cells(labyrinth: Labyrinth, y: int, x: int, cell_type, keep: list = None):
    labyrinth.set_cell(y, x, cell_type)
    pos_set = {(y, x)}

    if keep is not None:
        temp = set(keep)
        temp.update(pos_set)
        keep[:] = list(temp)

    return list(pos_set)


def add_entrance_finish(labyrinth: Labyrinth):
    for i in range(1, labyrinth.width_):  # add entrance
        if labyrinth.cell_check_wall(1, i, False):
            labyrinth.set_cell(0, i, Cell.PATH)
            labyrinth.start_coord_ = (0, i)
            break

    for i in range(labyrinth.width_ - 2, 1, -1):  # add exit
        if labyrinth.cell_check_wall(labyrinth.height_ - 2, i, False):
            labyrinth.set_cell(labyrinth.height_ - 1, i, Cell.PATH)
            labyrinth.finish_coord_ = (labyrinth.height_ - 1, i)
            break
