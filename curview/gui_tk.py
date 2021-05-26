from tkinter import Tk
from gui_tk_utils.add_window import AddWindow

from core import cur_names_get


root = Tk()
root.config(background="#000")
AddWindow(
    root,
    cur_names=cur_names_get(
        path="configs",
        filename="parse.yaml"
    ),
).pack()
root.mainloop()
