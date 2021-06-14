from tkinter import Tk
from gui_tk_utils.add_window import AddWindow
#from gui_tk_utils.table_widget import Table

from core import cur_names_get


#######################################################
# menu widget developing

from gui_tk_utils.menu_widget import Menu

def print_hello():
    print("Hello (o´'∀'｀o)!")


from tkinter import Tk
root = Tk()
options_and_actions = (
    ("main", print_hello),
    ("graphics", print_hello),
)
Menu(root, options_and_actions).pack()
root.mainloop()


#######################################################


def unnecessary():
    root = Tk()

    path="configs"
    filename="parse.yaml"

    AddWindow(
        root,
        cur_names=cur_names_get(
            path=path,
            filename=filename,
        ),
        path=path,
        filename=filename,
    ).pack()
    root.mainloop()
