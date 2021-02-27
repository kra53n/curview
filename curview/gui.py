from tkinter import (
    Tk,
    Button,
    Frame,
    Label,
    Entry,
    StringVar,
    PhotoImage,
)
from tkinter.ttk import Combobox

from yaml import safe_load as yaml_safe_load


# ------------------------------------------------------ #
# ------------- Cofnigure tkinter elements ------------- #
# ------------------------------------------------------ #
class ButtonMenu(Button):
    '''Set default Button from tkinter our settings
    for menu
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         **kwargs,
                         background = BACKGROUND,
                         activebackground = BACKGROUNDACTIVE,
                         foreground = FOREGROUND,
                         activeforeground = FOREGROUNDACTIVE,
                         bd = 0,
                         )


# --------------------------------------------------- #
# ----------------------- GUI ----------------------- #
# --------------------------------------------------- #
class CurViewGui:
    def __init__(self, master):
        ### GENERATION OF USER INTERFACE
        self.master = master
        # set geomtry of interface
        self.master.geometry('768x432')
        # set icon
        # first argument mean that tk will use it for children too
        self.master.iconphoto(True, PhotoImage(file='assets/lightning.png'))
        # set size after that we can`t change the size of window
        self.master.minsize(768, 432)
        # identify width
        self.width = master.winfo_screenwidth()
        # give title
        if self.width > 400:
            self.master.title('CurView - Currency view')
        else:
            self.master.title('CurView')
        # set color for background of app
        master.configure(background = BACKGROUNDAPP)

        # create frames
        self.create_frame_menu()
        self.create_frame_main()

        # create widgets
        self.create_widgets()

    def create_frame_menu(self):
        '''Creates menu bar frame
        '''
        self.frame_menu = Frame(self.master, bg = FOREGROUND)
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
        Button(self.frame_main,
               text = 'Quit',
               command = self.master.quit,
               bd = 0,
               background = BACKGROUND,
               activebackground = BACKGROUNDACTIVE,
               foreground = FOREGROUND,
               activeforeground = FOREGROUNDACTIVE,
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
        self.add_window_frame_main = Frame(self.add_window,
                                           background = BACKGROUNDAPP)
        self.add_window_frame_main.pack(padx = 3, pady = 6)
        # set colors
        self.add_window.configure(bg = BACKGROUNDAPP)
        Label(self.add_window_frame_main,
              text = 'Currency',
              bd = 0,
              background = BACKGROUNDAPP,
              foreground = BACKGROUND,
              ).grid(row = 0, column = 0)
        Label(self.add_window_frame_main,
              text = 'Amount',
              bd = 0,
              background = BACKGROUNDAPP,
              foreground = BACKGROUND,
              ).grid(row = 0, column = 1,)
        Button(self.add_window_frame_main,
               text = 'Add',
               background = BACKGROUND,
               activebackground = BACKGROUNDAPP,
               foreground = BACKGROUNDAPP,
               activeforeground = BACKGROUND,
               command = self.add_inf_cmd,
               bd = 0).grid(row = 0, column = 2,
                            sticky = 'nswe', padx = 3)
        self.add_inf_combobox = Combobox(self.add_window_frame_main,
            textvariable = self.add_window_countryvar,
            values = list_curs_name(),
            state = 'readonly'
            )
        self.add_inf_combobox.grid(row = 1, column = 0, padx = 3)
        self.add_inf_combobox.current(0)
        self.entry_add_inf = Entry(self.add_window_frame_main,
                                   background = BACKGROUND,
                                   foreground = FOREGROUND,
                                   bd = 0)
        self.entry_add_inf.grid(row = 1, column = 1, padx = 3)
        Button(self.add_window_frame_main,
               text = 'Close',
               background = BACKGROUND,
               activebackground = BACKGROUNDAPP,
               foreground = BACKGROUNDAPP,
               activeforeground = BACKGROUND,
               command = self.add_window.destroy,
               bd = 0,
               ).grid(row = 1, column = 2,
                      sticky = 'nswe', padx = 3)

    def add_inf_cmd(self):
        # TODO: make doc for this func
        from core import cur_put_db
        cur = str(self.add_inf_combobox.get())
        amount = float(self.entry_add_inf.get())
        cur_put_db(cur, amount)

    def shut_up_pc(self):
        print('Your PC already shut down')


if __name__ == '__main__':
    # ------------------------------------------- #
    # ---- START - INITIALIZE - COLORS ---------- #
    with open("assets/colors.yaml", 'r') as f:
        data = yaml_safe_load(f)
    for i in data.items():
        exec("{} = '{}'".format(i[0].upper(), i[1]))
    # ------ END - INITIALIZE - COLORS -  ------- #
    # ------------------------------------------- #
    root = Tk()
    gui = CurViewGui(root)
    root.mainloop()
