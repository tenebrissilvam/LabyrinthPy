from globals import Globals
import src.Entities.labyrinth

import src.Labyrinth_generation.binary_tree_generation
import src.Labyrinth_generation.DFS_generation
import src.Labyrinth_generation.MST_Kruskals_generation
import src.Labyrinth_generation.MST_Prims_generation
import src.Labyrinth_generation.Wilsons_generation

import src.Labyrinth_solution.solution

import tkinter

from tkinter import Label, Text, END, TOP, Entry, Scrollbar, RIGHT, Y


def run_in_window():
    Globals.window.title("LabyrinthPy")
    Globals.window.geometry('1000x800')

    scrollbar = Scrollbar(Globals.window)
    scrollbar.pack(side=RIGHT, fill=Y)

    lab_title = Label(Globals.window, text='Enter option to continue')
    lab_title.pack()

    Globals.value_inside.set("Select an Option")

    question_menu = tkinter.OptionMenu(Globals.window, Globals.value_inside, *Globals.options_list)
    question_menu.pack()

    submit_button = tkinter.Button(Globals.window, text='Submit', command=print_answers)
    submit_button.pack()

    Globals.window.mainloop()


def gen_lab():
    match Globals.gen_option:
        case 'DFS':
            Globals.m = src.Labyrinth_generation.DFS_generation.generate_dfs(Globals.w, Globals.h)
        case 'MinimalSpanningTree Prims':
            Globals.m = src.Labyrinth_generation.MST_Prims_generation.generate_mst_prims(Globals.w, Globals.h)
        case 'MinimalSpanningTree Kruskals':
            Globals.m = src.Labyrinth_generation.MST_Kruskals_generation.generate_mst_kruskals(Globals.w, Globals.h)
        case 'Binary tree':
            Globals.m = src.Labyrinth_generation.binary_tree_generation.generate_binary_tree(Globals.w, Globals.h)
        case 'Wilsons':
            Globals.m = src.Labyrinth_generation.Wilsons_generation.generate_wilsons(Globals.w, Globals.h)
        case _:
            print('option not chosen')


def print_solution():
    clear_window()
    src.Labyrinth_solution.solution.show_solution(Globals.m)
    text = Text(Globals.window, width=(Globals.w + 1) * 4 - 2, height=(Globals.h + 1) * 2 - 1)
    for i in range(Globals.m.height_):
        for j in range(Globals.m.width_):
            if Globals.m.cell_check_solved_wall(i, j, True):
                text.insert(END, u"\u2588\u2588")
            elif Globals.m.cell_check_solved_sol(i, j, True):
                text.insert(END, u"\u2592\u2592")
            else:
                text.insert(END, "  ")
        if not (i == Globals.m.height_ - 1):
            text.insert(END, '\n')
    text.pack()

    clear_button = tkinter.Button(Globals.window, text='Erase', command=clear_window)
    clear_button.pack(side=TOP)


def show_plot():
    text = Text(Globals.window, width=(Globals.w + 1) * 4 - 2, height=(Globals.h + 1) * 2 - 1)
    for i in range(Globals.m.height_):
        for j in range(Globals.m.width_):
            if Globals.m.cell_check_wall(i, j, True):
                text.insert(END, u"\u2588\u2588")
            else:
                text.insert(END, "  ")
        if not (i == Globals.m.height_ - 1):
            text.insert(END, '\n')
    text.pack()

    save_button = tkinter.Button(Globals.window, text='Save as .txt', command=save_to_txt)
    save_button.pack()

    clear_button = tkinter.Button(Globals.window, text='Erase', command=clear_window)
    clear_button.pack(side=TOP)

    solve_button = tkinter.Button(Globals.window, text='Show Solution', command=print_solution)
    solve_button.pack(side=TOP)


def clear_window():
    flag = False
    for widget in Globals.window.winfo_children():
        if widget.widgetName == "text" or flag:
            flag = True
            widget.destroy()


def print_answers():
    print("Selected Option: {}".format(Globals.value_inside.get()))
    match Globals.value_inside.get():
        case 'Generate labyrinth':
            generate_visuals()
        case 'Upload labyrinth':
            recognize_visuals()
        case _:
            pass


def generate_visuals():

    val_inside = tkinter.StringVar(Globals.window)
    val_inside.set("Select an Option")

    params_label = Label(Globals.window, text='Choose generation algorithm')
    params_label.pack()

    gen_question_menu = tkinter.OptionMenu(Globals.window, val_inside, *Globals.options_for_generation)
    gen_question_menu.pack()

    params_label = Label(Globals.window, text='Enter width and height (Recommended range of values [1;25])')
    params_label.pack()

    width = Entry(Globals.window, )
    width.pack(side=TOP)
    height = Entry(Globals.window, )
    height.pack(side=TOP)

    def get_size():
        Globals.w = int(width.get())

        Globals.h = int(height.get())
        print(Globals.w, Globals.h)

        Globals.gen_option = val_inside.get()
        gen_lab()
        show_plot()

    button0 = tkinter.Button(Globals.window, text="Enter", command=get_size)
    button0.pack(side=TOP)


def recognize():
    with open(Globals.save_filepath, 'r') as f:
        lines = f.readlines()

        Globals.w = (len(lines[0])) // 6
        Globals.h = len(lines) // 2
        Globals.m = src.Entities.labyrinth.Labyrinth(Globals.w, Globals.h, src.Entities.labyrinth.Cell.WALL)

        y = 0

        print(Globals.w, Globals.h)

        for line in lines:
            for x in range(0, len(line), 3):
                if y == 0 and line[x] == " ":
                    Globals.m.start_coord_ = (0, x // 3)
                if y == Globals.h - 1 and line[x] == " ":
                    Globals.m.finish_coord_ = (2 * y + 2, x // 3)
                if line[x] == u"\u2588":
                    Globals.m.set_cell(y, x // 3, src.Entities.labyrinth.Cell.WALL)
                elif line[x] == " ":
                    Globals.m.set_cell(y, x // 3, src.Entities.labyrinth.Cell.PATH)
            y += 1
        print('reading complete')

    show_plot()


def recognize_visuals():
    get_path_read()
    print(Globals.save_filepath)


def get_path_read():
    file_title = Label(Globals.window, text='Enter filepath')
    file_title.pack()

    filepath = Entry(Globals.window, )
    filepath.pack(side=TOP)

    def get_filepath_read():  # needs fixing
        print(filepath.get())
        if not (filepath.get() == ''):
            Globals.save_filepath = filepath.get()
        recognize()

    button3 = tkinter.Button(Globals.window, text="Enter", command=get_filepath_read)
    button3.pack(side=TOP)


def get_path():
    file_title = Label(Globals.window, text='Enter filepath')
    file_title.pack()

    filepath = Entry(Globals.window, )
    filepath.pack(side=TOP)

    def get_filepath():  # needs fixing
        print(filepath.get())
        if not (filepath.get() == ''):
            Globals.save_filepath = filepath.get()
        save_fin()

    button3 = tkinter.Button(Globals.window, text="Enter", command=get_filepath)
    button3.pack(side=TOP)


def save_fin():
    with open(Globals.save_filepath, 'w+') as f:
        for i in range(Globals.m.height_):
            for j in range(Globals.m.width_):
                if Globals.m.cell_check_wall(i, j, True):
                    f.write(u"\u2588\u2588\u2588")
                else:
                    f.write("   ")
            f.write('\n')
    print('saving complete')


def save_to_txt():
    get_path()
    print(Globals.save_filepath)


run_in_window()
