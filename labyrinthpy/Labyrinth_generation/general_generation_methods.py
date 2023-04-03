def update_cells(labyrinth, y, x, cell_type, keep: list = None):
    labyrinth.set_cell(y, x, cell_type)
    pos_set = {(y, x)}

    if keep is not None:
        temp = set(keep)
        temp.update(pos_set)
        keep[:] = list(temp)
    '''
    if destroy is not None:
        for i in pos_set:
            destroy.remove(i)
    '''
    return list(pos_set)


