import tkinter

import labyrinthpy.Labyrinth_generation.DFS_generation
import labyrinthpy.Labyrinth_generation.MST_Prims_generation
import labyrinthpy.Labyrinth_generation.MST_Kruskals_generation
import labyrinthpy.Labyrinth_solution.solution
import labyrinthpy.Entities.labyrinth

from tkinter import *

w = 0
h = 0
gen_option = ''
m = labyrinthpy.Entities.labyrinth.Labyrinth()

window = Tk()
window.title("LabyrinthPy")
window.geometry('1000x800')

lab_title = Label(window, text='Enter option to continue')
lab_title.pack()

options_list = ['Generate labyrinth', 'Upload labyrinth']
options_for_generation = ['DFS', 'MinimalSpanningTree Prims', 'MinimalSpanningTree Kruskals']

value_inside = tkinter.StringVar(window)
value_inside.set("Select an Option")

question_menu = tkinter.OptionMenu(window, value_inside, *options_list)
question_menu.pack()


def gen_lab():
    global m
    if gen_option == 'DFS':
        m = labyrinthpy.Labyrinth_generation.DFS_generation.generate_dfs(w, h)
    elif gen_option == 'MinimalSpanningTree Prims':
        m = labyrinthpy.Labyrinth_generation.MST_Prims_generation.generate_mst_prims(w, h)
    elif gen_option == 'MinimalSpanningTree Kruskals':
        m = labyrinthpy.Labyrinth_generation.MST_Prims_generation.generate_mst_prims(w, h)


def print_solution():
    clear_window()
    labyrinthpy.Labyrinth_solution.solution.show_solution(m)
    text = Text(window, width=(w + 1) * 4 - 2, height=(h + 1) * 2 - 1)
    for i in range(m.height_):
        for j in range(m.width_):
            if m.cell_check_solved_wall(i, j, True):
                text.insert(END, u"\u2588\u2588")
            elif m.cell_check_solved_sol(i, j, True):
                text.insert(END, u"\u2592\u2592")
            else:
                text.insert(END, "  ")
        if not (i == m.height_ - 1):
            text.insert(END, '\n')
    text.pack()

    clear_button = tkinter.Button(window, text='Erase', command=clear_window)
    clear_button.pack(side=TOP)


def show_plot():
    text = Text(window, width=(w + 1) * 4 - 2, height=(h + 1) * 2 - 1)
    for i in range(m.height_):
        for j in range(m.width_):
            if m.cell_check_wall(i, j, True):
                text.insert(END, u"\u2588\u2588")
            else:
                text.insert(END, "  ")
        if not (i == m.height_ - 1):
            text.insert(END, '\n')
    text.pack()

    clear_button = tkinter.Button(window, text='Erase', command=clear_window)
    clear_button.pack(side=TOP)

    solve_button = tkinter.Button(window, text='Show Solution', command=print_solution)
    solve_button.pack(side=TOP)


def clear_window():
    flag = False
    for widget in window.winfo_children():
        if widget.widgetName == "text" or flag:
            flag = True
            widget.destroy()


def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    if value_inside.get() == 'Generate labyrinth':
        Generate()
    elif value_inside.get() == 'Upload labyrinth':
        pass
    else:
        pass
    return None


def Generate():
    global gen_option

    val_inside = tkinter.StringVar(window)
    val_inside.set("Select an Option")

    params_label = Label(window, text='Choose generation algorithm')
    params_label.pack()

    gen_question_menu = tkinter.OptionMenu(window, val_inside, *options_for_generation)
    gen_question_menu.pack()

    params_label = Label(window, text='Enter width and height (Recommended range of values [1;25])')
    params_label.pack()

    width = Entry(window, )
    width.pack(side=TOP)
    height = Entry(window, )
    height.pack(side=TOP)

    def get_size():
        global w
        w = int(width.get())
        global h
        h = int(height.get())
        print(w, h)
        global gen_option
        gen_option = val_inside.get()
        gen_lab()
        show_plot()

    button0 = tkinter.Button(window, text="Enter", command=get_size)
    button0.pack(side=TOP)


submit_button = tkinter.Button(window, text='Submit', command=print_answers)
submit_button.pack()

window.mainloop()
