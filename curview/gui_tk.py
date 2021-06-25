from tkinter import Tk
from gui_tk_utils.add_window import AddWindow

from core import cur_names_get



def add_window_test():
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


if __name__ == "__main__":
    add_window_test()
