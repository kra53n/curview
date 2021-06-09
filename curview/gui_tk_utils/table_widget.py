from tkinter import Frame
from .style import LabelAddWindow


class Table(Frame):
    def __init__(self, main, row, **kwargs):
        """
        + ---------------------- ARGUMENTS --------------------- +
        | row - thing from what builded the table widget         |
        + ------------------------------------------------------ +
        """
        self.main = main
        Frame.__init__(self, self.main)
        self.row = row
        self.__init_table()
        if kwargs["background"]:
            self.main.config(background=kwargs["background"])

    def __init_table(self):
        for i in range(len(self.row)):
            for j in range(len(self.row[0])):
                LabelAddWindow(
                    self.main,
                    text=self.row[i][j]
                ).grid(row=i, column=j)
