import tkinter

import src.Labyrinth_generation.DFS_generation
import src.Labyrinth_generation.MST_Prims_generation
import src.Labyrinth_generation.MST_Kruskals_generation
import src.Labyrinth_solution.solution
import src.Entities.labyrinth

from tkinter import *

w = 0
h = 0
gen_option = ''
m = src.Entities.labyrinth.Labyrinth()
save_filepath = 'LabyrinthPyLab.txt'

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
        m = src.Labyrinth_generation.DFS_generation.generate_dfs(w, h)
    elif gen_option == 'MinimalSpanningTree Prims':
        m = src.Labyrinth_generation.MST_Prims_generation.generate_mst_prims(w, h)
    elif gen_option == 'MinimalSpanningTree Kruskals':
        m = src.Labyrinth_generation.MST_Kruskals_generation.generate_mst_prims(w, h)


def print_solution():
    clear_window()
    src.Labyrinth_solution.solution.show_solution(m)
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

    save_button = tkinter.Button(window, text='Save as .txt', command=save_to_txt)
    save_button.pack()

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
        generate_visuals()
    elif value_inside.get() == 'Upload labyrinth':
        recognize_visuals()
    else:
        pass


def generate_visuals():
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


def recognize():
    with open(save_filepath, 'r') as f:
        lines = f.readlines()
        global m
        global h
        global w
        w = ((len(lines[0]) - 1) // 2) // 3
        h = (len(lines) - 1) // 2
        m = src.Entities.labyrinth.Labyrinth((len(lines) - 1) // 2, ((len(lines[0]) - 1) // 2) // 3,
                                             src.Entities.labyrinth.Cell.WALL)
        y = 0
        print(len(lines), (len(lines) - 1) // 2, len(lines[0]), ((len(lines[0]) - 1) // 2) // 3)
        for line in lines:
            for x in range(0, (len(lines) - 1) // 2, 3):
                if line[x] == u"\u2588":
                    m.set_cell(y, x, src.Entities.labyrinth.Cell.WALL)
                elif line[x] == " ":
                    m.set_cell(y, x, src.Entities.labyrinth.Cell.PATH)
            y += 1
        print('reading complete')
    show_plot()


def recognize_visuals():
    get_path_read()
    print(save_filepath)


def get_path_read():
    file_title = Label(window, text='Enter filepath')
    file_title.pack()

    filepath = Entry(window, )
    filepath.pack(side=TOP)

    def get_filepath_read():  # needs fixing
        global save_filepath
        print(filepath.get())
        if not (filepath.get() == ''):
            save_filepath = filepath.get()
        recognize()

    button3 = tkinter.Button(window, text="Enter", command=get_filepath_read)
    button3.pack(side=TOP)


def get_path():
    file_title = Label(window, text='Enter filepath')
    file_title.pack()

    filepath = Entry(window, )
    filepath.pack(side=TOP)

    def get_filepath():  # needs fixing
        global save_filepath
        print(filepath.get())
        if not (filepath.get() == ''):
            save_filepath = filepath.get()
        save_fin()

    button3 = tkinter.Button(window, text="Enter", command=get_filepath)
    button3.pack(side=TOP)


def save_fin():
    with open(save_filepath, 'w+') as f:
        for i in range(m.height_):
            for j in range(m.width_):
                if m.cell_check_wall(i, j, True):
                    f.write(u"\u2588\u2588\u2588")
                else:
                    f.write("   ")
            f.write('\n')
    print('saving complete')


def save_to_txt():
    get_path()
    print(save_filepath)


submit_button = tkinter.Button(window, text='Submit', command=print_answers)
submit_button.pack()

window.mainloop()
