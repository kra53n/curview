"""
This is main window of tkinter app.

Right now it is thing that just can add currency to db.
"""

from tkinter import Tk
#from style import ButtonMenu
#from style import colors


class MainWindow:
    def __init__(self, main):
        self.main = main
        self.main.configure(background=colors["backgroundapp"])
