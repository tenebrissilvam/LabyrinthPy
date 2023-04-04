import tkinter

import labyrinthpy.Labyrinth_generation.DFS_generation
import labyrinthpy.Labyrinth_generation.MST_Prims_generation
import labyrinthpy.Labyrinth_generation.MST_Kruskals_generation

import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("LabyrinthPy")
window.geometry('1000x800')

options_list = ['Generate labyrinth', 'Upload labyrinth']
options_for_generation = ['DFS', 'MinimalSpanningTree Prims', 'MinimalSpanningTree Kruskals']

value_inside = tkinter.StringVar(window)
value_inside.set("Select an Option")

question_menu = tkinter.OptionMenu(window, value_inside, *options_list)
question_menu.pack()


def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    if value_inside.get() == 'Generate labyrinth':
        val_inside = tkinter.StringVar(window)
        val_inside.set("Select an Option")

        gen_question_menu = tkinter.OptionMenu(window, val_inside, *options_for_generation)
        gen_question_menu.pack()

        def show_lab():
            w = int(width.get())
            h = int(height.get())

            if val_inside.get() == 'DFS':
                m = labyrinthpy.Labyrinth_generation.DFS_generation.generate_dfs(w, h)
            elif val_inside.get() == 'MinimalSpanningTree Prims':
                m = labyrinthpy.Labyrinth_generation.MST_Prims_generation.generate_mst_prims(w, h)
            elif val_inside.get() == 'MinimalSpanningTree Kruskals':
                m = labyrinthpy.Labyrinth_generation.MST_Prims_generation.generate_mst_prims(w, h)

            text = Text(window, width=(w + 1) * 4 - 1, height=(h + 1) * 2 - 1)
            for i in range(m.height_):
                for j in range(m.width_):
                    if m.cell_check(i, j, True):
                        text.insert(END, u"\u2588\u2588")
                    else:
                        text.insert(END, "  ")
                text.insert(END, '\n')
            text.pack()

            def erase_text():
                text.delete("1.0", END)

            def remove_widget():
                text.place_forget()

            # button1 = tkinter.Button(window, text="Insert", command=insert_text)
            # button1.pack(side=TOP)
            # button2 = tkinter.Button(window, text="Erase", command=remove_widget())
            # button2.pack(side=TOP)

        width = Entry(window, )
        width.pack(side=TOP)
        height = Entry(window, )
        height.pack(side=TOP)

        button0 = tkinter.Button(window, text="Enter", command=show_lab)
        button0.pack(side=TOP)
    elif value_inside.get() == 'Upload labyrinth':
        pass
    else:
        pass
    return None


submit_button = tkinter.Button(window, text='Submit', command=print_answers)
submit_button.pack()

window.mainloop()
