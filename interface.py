import time
import tkinter as tk
from tkinter import *
import easygui

import sys


import subprocess

w = tk.Tk()
w.title("TeaRedactor")
w.tk.call("wm", "iconphoto", w._w, tk.PhotoImage(file="templates/img.png"))
entry = tk.Text()


def newfile():
    def get_entry():
        value = filename.get()
        if value:

            with open(f"C:/Users/vorob/OneDrive/Рабочий стол/TeaRedactor/{value}.py", 'w', encoding="utf-8") as file:
                pass

            filename.destroy()
            okay.destroy()

        else:
            print("Empty")

    filename = Entry(w)
    okay = Button(w, command=get_entry, text="OK")
    filename.pack()
    okay.pack()

    return filename


def openfile():
    global entry
    input_file = easygui.fileopenbox(filetypes=["*.py"])
    print(input_file)

    with open(input_file, "r", encoding="utf-8") as file:
        code = file.readlines()
        print(code)

    entry.delete(0.0, END)
    for string in code[::-1]:
        entry.insert(0.0, string)

    return


def saveas():
    global entry
    code = entry.get(1.0, END)
    path = easygui.diropenbox()

    def get_entry():            # два раза написан один и тот же кусок кода
        value = filename.get()
        if value:
            with open(f"{path}/{value}.py", 'w', encoding="utf-8") as file:
                file.write(code)

            filename.destroy()
            okay.destroy()

        else:
            print("Empty")

    filename = Entry(w)
    okay = Button(w, command=get_entry, text="OK")
    filename.pack()
    okay.pack()


def save():
    pass


def delete():
    pass


def exit():
    sys.exit()


def runcode():
    code = entry.get(1.0, END)   # работает только через консоль pycharm
    exec(code)

def blackt():
    entry.tag_add("here", "1.0", "1.0")
    entry.tag_config({"background": "black"}) # GOVNO НЕ РАБОТАЕТ

def mainloop():

    mainmenu = Menu(w)
    w.config(menu=mainmenu)

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="New", command=newfile)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command=NONE)
    filemenu.add_command(label="Save as...", command=saveas)
    filemenu.add_command(label="Delete", command=NONE)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit)

    runmenu = Menu(mainmenu, tearoff=0)
    runmenu.add_command(label="Run", command=runcode)
    runmenu.add_command(label="Stop", command=NONE)
    runmenu.add_command(label="Debug", command=NONE)

    thememenu = Menu(mainmenu, tearoff=0)
    thememenu.add_command(label="White", command=NONE)
    thememenu.add_command(label="Black", command=blackt)
    thememenu.add_command(label="Color", command=NONE)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="Help?", command=NONE)

    mainmenu.add_cascade(label="File", menu=filemenu)
    mainmenu.add_cascade(label="Run", menu=runmenu)
    mainmenu.add_cascade(label="Theme", menu=thememenu)
    mainmenu.add_cascade(label="Help", menu=helpmenu)

    entry.pack()

    w.mainloop()

