from tkinter import Frame
from tkinter import StringVar
from tkinter.ttk import Combobox

from .style import ButtonAddWindow
from .style import LabelAddWindow
from .style import EntryAddWindow
from .style import colors


class AddWindow:
    def __init__(self, main, **kwargs):
        self.main = main
        self.main.title("Add")
        self.main.resizable(0, 0)
        self.main.config(bg=colors["backgroundapp"])

        self.main_frame = Frame(
            self.main,
            background=colors["backgroundapp"],
        )
        self.main_frame.pack(padx=3, pady=6)

        LabelAddWindow(
            self.main_frame,
            text="Currency",
        ).grid(row=0, column=0)
        LabelAddWindow(
            master=self.main_frame, text="Amount",
        ).grid(row=0, column=1)

        ButtonAddWindow(
            self.main_frame,
            text="Add",
            command=self.add_inf,
        ).grid(row=0, column=2, sticky="nswe", padx=3)

        self.count_var = StringVar()
        self.combobox = Combobox(
            self.main_frame,
            textvariable=self.count_var,
            values=kwargs["cur_names"],
            state="readonly",
        )
        self.combobox.grid(row=1, column=0, padx=3)

        self.entry = EntryAddWindow(self.main_frame)
        self.entry.grid(row=1, column=1, padx=3)

        ButtonAddWindow(
            self.main_frame,
            text="Close",
            command=self.main.destroy
        ).grid(
            row=1, column=2, sticky="nswe", padx=3,
        )

    def add_inf(self):
        #from ..gui_tk import Cmds
        #curname = self.combobox.get()
        #amount = self.entry.get()

        #Cmds.add_inf(
        #    cur_name=curname,
        #    amount=amount,
        #)
        pass
