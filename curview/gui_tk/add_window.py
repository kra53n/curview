from tkinter import Frame
from tkinter import Label

from style import colors
from style import LabelAddWindow
from style import ButtonAddWindow


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

        LabelAddWindow(self.main_frame, text="Currency").grid(row=0, column=0)
        LabelAddWindow(self.main_frame, text="Amount").grid(row=0, column=1)

        ButtonAddWindow(self.main_frame, text="Add").grid(
            row=0, column=2, sticky="nswe", padx=3,
        )
