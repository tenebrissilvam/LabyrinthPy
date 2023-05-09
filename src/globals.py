import src.Entities.labyrinth
import tkinter
from tkinter import Tk


class Globals:
    w = 0
    h = 0

    gen_option = ''
    save_filepath = 'generated_labyrinthPy'

    m = src.Entities.labyrinth.Labyrinth()

    window = Tk()
    value_inside = tkinter.StringVar(window)

    options_list = ['Generate labyrinth', 'Upload labyrinth']
    options_for_generation = ['DFS', 'MinimalSpanningTree Prims', 'MinimalSpanningTree Kruskals',
                              'Binary tree', 'Wilsons']
