from tkinter import Tk
from gui_tk_utils.add_window import AddWindow

from core import cur_names_get


root = Tk()
AddWindow(
    root,
    cur_names=cur_names_get(
        path="configs",
        filename="parse.yaml"
    ),
)
root.mainloop()
