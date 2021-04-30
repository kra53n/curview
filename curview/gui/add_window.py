from tkinter import Tk
from tkinter import StringVar
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter.ttk import Combobox


class AddWindow:
    def __ini__(
        self,
        master,
        backgroundapp,
        background,
        foreground,
        activebackground,
        activeforeground,
    ):
        '''Function create new window where user can
        put his values
        '''
        # from core import list_curs_name

        self.backgroundapp = backgroundapp
        self.background = background
        self.foreground = foreground
        self.activebackground = activebackground
        self.activeforeground = activeforeground

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
        # from core import cur_put_db

        cur = str(self.add_inf_combobox.get())
        amount = float(self.entry_add_inf.get())
        cur_put_db(cur, amount)


def add_window(
        backgroundapp="#2C3531",
        background="#D1E8E2",
        foreground="#116466",
        activebackground="#116466",
        activeforeground="#D1E8E2",
    ):
    root = Tk()
    gui = AddWindow()
    # gui = AddWindow(
    #     root,
    #     backgroundapp,
    #     background,
    #     foreground,
    #     activebackground,
    #     activeforeground
    # )
    root.mainloop()
