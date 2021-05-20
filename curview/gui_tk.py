from tkinter import Tk
import os.path
from yaml import safe_load

from gui_tk_utils.add_window import AddWindow

# parse colors.yaml and return as dict(name: color code).
# for example: "background": "#777777"
with open(os.path.join("configs", "colors.yaml")) as f:
    colors = safe_load(f)


root = Tk()
AddWindow(root)
root.mainloop()
