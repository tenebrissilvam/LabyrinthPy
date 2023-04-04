import tkinter

import labyrinthpy.Labyrinth_generation.DFS_generation
import labyrinthpy.Labyrinth_generation.MST_Prims_generation
import labyrinthpy.Labyrinth_generation.MST_Kruskals_generation

import tkinter as tk
from tkinter import *
from tkinter import messagebox

# m = labyrinthpy.Labyrinth_generation.DFS_generation.generate_dfs(30, 10)

# m = labyrinthpy.Labyrinth_generation.MST_Prims_generation.generate_mst_prims(30, 30)

# m.visualize()

window = Tk()  # Создаём окно приложения.
window.title("LabyrinthPy")  # Добавляем название приложения.
window.geometry('1000x800')

options_list = ['Generate labyrinth', 'Upload labyrinth']

value_inside = tkinter.StringVar(window)
value_inside.set("Select an Option")

question_menu = tkinter.OptionMenu(window, value_inside, *options_list)
question_menu.pack()


def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    if value_inside.get() == 'Generate labyrinth':
        # m = labyrinthpy.Labyrinth_generation.DFS_generation.generate_dfs(30, 10)
        w = 12
        h = 12
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
            
        # button1 = tkinter.Button(window, text="Insert", command=insert_text)
        # button1.pack(side=TOP)
        button2 = tkinter.Button(window, text="Erase", command=erase_text)
        button2.pack(side=TOP)
    elif value_inside.get() == 'Upload labyrinth':
        pass
    else:
        pass
    return None


submit_button = tkinter.Button(window, text='Submit', command=print_answers)
submit_button.pack()
'''
frame = Frame(
   window, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 #Задаём отступ по вертикали.
)

frame.pack(expand=True) #Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.

height_lb = Label(
   frame,
   text="Введите   "
)
height_lb.grid(row=3, column=1)


'''

window.mainloop()
