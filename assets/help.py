'''
Help to choose color for gui
'''

from tkinter import Tk, Button
from json import load


class HelpGui:
    def __init__(self, master):
        self.master = master
        self.master.resizable(0, 0)
        self.master.configure(background = '#111')
        self.create_widgets()

    def create_widgets(self):
        m = load_colors()
        for i in range(len(m)):
            Button(self.master,
                   bd = 0,
                   text = m[i][0],
                   background = m[i][1],
                   foreground = '#111',
                   activebackground = '#111',
                   ).pack(fill = 'x', ipady = 10, pady = 2)


### FUNTCIONS
def load_colors():
    with open('colors.json', 'r') as f:
        data = load(f)
    return tuple(data.items())


if __name__ == '__main__':
    root = Tk()
    gui = HelpGui(root)
    root.mainloop()
