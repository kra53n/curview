from tkinter import Frame
from tkinter import Label
from tkinter import StringVar
from tkinter.ttk import Combobox

from .style import LabelAddWindow
from .style import ButtonAddWindow


class AddWindow:
    def __init__(self, main):
        self.main = main
        self.main.title("Add")
        self.main.resizable(0, 0)
        #self.main.config(bg=colors["backgroundapp"])

        self.main_frame = Frame(
            self.main,
            #background=colors["backgroundapp"],
        )
        self.main_frame.pack(padx=3, pady=6)

        LabelAddWindow(
            self.main_frame, text="Currency",
        ).grid(row=0, column=0)
        LabelAddWindow(
            self.main_frame, text="Amount",
        ).grid(row=0, column=1)

        ButtonAddWindow(
            self.main_frame, text="Add",
        ).grid(row=0, column=2, sticky="nswe", padx=3)

        #self.curnames = curnames
        self.count_var = StringVar()
        self.add_combobox = Combobox(
            self.main_frame,
            textvariable=self.count_var,
            #values=self.curnames,
            state="readonly",
        )
        self.add_combobox.grid(row=1, column=0, padx=3)
        #self.add_combobox.current(0)
