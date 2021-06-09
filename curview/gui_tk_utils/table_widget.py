from tkinter import Frame
from .style import LabelAddWindow


class Table(Frame):
    def __init__(self, main, rows, **kwargs):
        """
        + ---------------------- ARGUMENTS --------------------- +
        | rows - thing from what builded the table widget        |
        + ------------------------------------------------------ +
        """
        self.main = main
        Frame.__init__(self, self.main)
        self.rows = rows
        self.__init_table()
        if kwargs["background"]:
            self.main.config(background=kwargs["background"])

    def __init_table(self):
        for i in range(len(self.rows)):
            for j in range(len(self.rows[0])):
                LabelAddWindow(
                    self.main,
                    text=self.rows[i][j]
                ).grid(row=i, column=j)
