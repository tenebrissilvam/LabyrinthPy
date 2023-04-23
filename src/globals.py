import src.Entities.labyrinth
import tkinter
from tkinter import Label, Tk, Text, END, TOP, Entry, Scrollbar, RIGHT, Y


w = 0
h = 0
gen_option = ''
m = src.Entities.labyrinth.Labyrinth()
save_filepath = 'LabyrinthPyLab.txt'
window = Tk()
value_inside = tkinter.StringVar(window)
options_list = ['Generate labyrinth', 'Upload labyrinth']
options_for_generation = ['DFS', 'MinimalSpanningTree Prims', 'MinimalSpanningTree Kruskals',
                          'Binary tree', 'Wilsons']

