from tkinter import Frame
from tkinter import StringVar
from tkinter.ttk import Combobox

from core import exactly_time
from core import wwdb
from core import date

from .style import ButtonAddWindow
from .style import LabelAddWindow
from .style import EntryAddWindow
from .style import colors


class AddWindow(Frame):
    def __init__(self, main, **kwargs):
        Frame.__init__(self, main)

        # path to configs
        self.path = kwargs["path"]
        # path to parse.yaml
        self.filename = kwargs["filename"]
        # list of currencies in dict
        self.update_curs()

        self.main = main
        self.main.title("Add")
        self.main.config(bg=colors["backgroundapp"])

        self.main_frame = Frame(
            self,
            background=colors["backgroundapp"],
        )
        self.main_frame.pack()

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
        self.combobox.current(0)

        self.entry = EntryAddWindow(self.main_frame)
        self.entry.grid(row=1, column=1, padx=3)

        ButtonAddWindow(
            self.main_frame,
            text="Close",
            command=self.main.destroy
        ).grid(
            row=1, column=2, sticky="nswe", padx=3,
        )

    def update_curs(self):
        """
        Update dict with currencies information
        """
        from core import cur_parse_all
        self.curs = cur_parse_all(self.path, self.filename)

    def add_inf(self):
        combobox = self.combobox.get()
        for cur_inf in self.curs:
            if combobox == cur_inf["name"]:
                cur = cur_inf
                break
        
        wwdb(
            db_name=str(exactly_time()[0])+".db",
            db_choice="write",
            currency=cur,
            amount=float(self.entry.get()),
            date=date(),
        )