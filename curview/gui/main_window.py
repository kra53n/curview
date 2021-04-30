from tkinter import Tk
from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter.ttk import Combobox

from widgets import ButtonMenu

from yaml import safe_load


class MainWindow:
    def __init__(
            self,
            master,
            backgroundapp,
            background,
            foreground,
            activebackground,
            activeforeground,
        ):
        self.backgroundapp = backgroundapp
        self.background = background
        self.foreground = foreground
        self.activebackground = activebackground
        self.activeforeground = activeforeground

        self.master = master
        self.master.geometry('768x432')
        self.master.iconphoto(True, PhotoImage(file='assets/lightning.png'))
        self.master.minsize(768, 432)
        self.width = master.winfo_screenwidth()
        self.master.title('Curview')
        master.configure(background = self.backgroundapp)

        # create frames
        self.create_frame_menu()
        self.create_frame_main()

        # create widgets
        self.create_widgets()

    def create_frame_menu(self):
        '''Creates menu bar frame
        '''
        self.frame_menu = Frame(self.master, bg = self.foreground)
        self.frame_menu.pack(side = 'left', fill = 'y', ipadx = 4)

    def create_frame_main(self):
        '''Create frame where we can see main information
        '''
        self.frame_main = Frame(self.master)
        self.frame_main.pack(expand = 1)

    def create_widgets_menu(self):
        '''Widgets that prossessed inf frame_menu
        '''
        ButtonMenu(self.frame_menu,
                   text = 'Add',
                   command = self.add_inf,
                   ).pack(fill = 'x', padx = 10, pady = 3)
        ButtonMenu(self.frame_menu,
                   text = 'Quit',
                   command = self.master.quit,
                   ).pack(fill = 'x', padx = 10, pady = 3)
        ButtonMenu(self.frame_menu,
                   text = 'Settings',
                   ).pack(fill = 'x', padx = 10, pady = 3)

    def create_widgets(self):
        '''Function create widgets
        '''
        self.create_widgets_menu()
        Button(
            self.frame_main,
            text = 'Quit',
            command = self.master.quit,
            bd = 0,
            background = self.background,
            activebackground = self.activebackground,
            foreground = self.foreground,
            activeforeground = self.activeforeground,
        ).pack()

    # action functions
    def add_inf(self):
        '''Function create new window where user can
        put his values
        '''
        from core import list_curs_name
        # interaction with interface
        self.add_window_countryvar = StringVar()
        # create window
        self.add_window = Tk()
        # create title of window
        self.add_window.title('Add')
        # paste inresize
        self.add_window.resizable(0, 0)
        # create frames
        self.add_window_frame_main = Frame(
            self.add_window,
            background = self.backgroundapp
        )
        self.add_window_frame_main.pack(padx = 3, pady = 6)
        # set colors
        self.add_window.configure(bg = self.backgroundapp)
        Label(
            self.add_window_frame_main,
            text = 'Currency',
            bd = 0,
            background = self.backgroundapp,
            foreground = self.background,
        ).grid(row = 0, column = 0)
        Label(
            self.add_window_frame_main,
            text = 'Amount',
            bd = 0,
            background = self.backgroundapp,
            foreground = self.background,
        ).grid(row = 0, column = 1,)
        Button(
            self.add_window_frame_main,
            text = 'Add',
            background = self.background,
            activebackground = self.backgroundapp,
            foreground = self.backgroundapp,
            activeforeground = self.background,
            command = self.add_inf_cmd,
            bd = 0
        ).grid(
            row = 0, column = 2,
            sticky = 'nswe', padx = 3
        )
        self.add_inf_combobox = Combobox(
            self.add_window_frame_main,
            textvariable = self.add_window_countryvar,
            values = list_curs_name(),
            state = 'readonly'
        )
        self.add_inf_combobox.grid(row = 1, column = 0, padx = 3)
        self.add_inf_combobox.current(0)
        self.entry_add_inf = Entry(
            self.add_window_frame_main,
            background = self.background,
            foreground = self.foreground,
            bd = 0
        )
        self.entry_add_inf.grid(row = 1, column = 1, padx = 3)
        Button(
            self.add_window_frame_main,
            text = 'Close',
            background = self.background,
            activebackground = self.backgroundapp,
            foreground = self.backgroundapp,
            activeforeground = self.background,
            command = self.add_window.destroy,
            bd = 0,
        ).grid(
            row = 1, column = 2,
            sticky = 'nswe', padx = 3
        )

    def add_inf_cmd(self):
        # TODO: make doc for this func
        from core import cur_put_db
        cur = str(self.add_inf_combobox.get())
        amount = float(self.entry_add_inf.get())
        cur_put_db(cur, amount)

def main_window():
    """
    Run MainWindow class
    """
    # set colors
    backgroundapp = "#2C3531"
    background = "#D1E8E2"
    foreground = "#116466"
    activebackground = "#116466"
    activeforeground = "#D1E8E2"

    root = Tk()
    gui = MainWindow(
        root,
        backgroundapp,
        background,
        foreground,
        activebackground,
        activeforeground
    )
    root.mainloop()
