from tkinter import Tk, Button, Frame, Label, Entry
from json import load as json_load


class CurViewGui:
    def __init__(self, master):
        ### GENERATION OF USER INTERFACE
        self.master = master
        # set geomtry of interface
        self.master.geometry('768x432')
        # set size after that we can`t change the size of window
        self.master.minsize(768, 432)
        # identify width
        self.width = master.winfo_screenwidth()
        # give title
        if self.width > 400:
            self.master.title('CurView - Currency view')
        else:
            self.master.title('CurView')
        # create colors from colors.json file
        self.create_colors()
        # set color for backgroudn of app
        master.configure(background = self.backgroundApp)
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
        Button(self.frame_menu,
               text = 'Add',
               bd = 0,
               background = self.background,
               activebackground = self.backgroundActive,
               foreground = self.foreground,
               activeforeground = self.foregroundActive,
               command = self.add_inf,
               ).pack(fill = 'x', padx = 10, pady = 3)
        Button(self.frame_menu,
               text = 'Main',
               bd = 0,
               background = self.background,
               activebackground = self.backgroundActive,
               foreground = self.foreground,
               activeforeground = self.foregroundActive,
               ).pack(fill = 'x', padx = 10, pady = 3)
        Button(self.frame_menu,
               text = 'Settings',
               bd = 0,
               background = self.background,
               activebackground = self.backgroundActive,
               foreground = self.foreground,
               activeforeground = self.foregroundActive,
               ).pack(fill = 'x', padx = 10, pady = 3)
        Button(self.frame_menu,
               text = 'Shut up PC',
               command = self.shut_up_pc,
               bd = 0,
               background = self.background,
               activebackground = self.backgroundActive,
               foreground = self.foreground,
               activeforeground = self.foregroundActive,
               ).pack(fill = 'x', padx = 10, pady = 3)

    def create_widgets(self):
        '''Function create widgets
        '''
        self.create_widgets_menu()
        Button(self.frame_main,
               text = 'Quit',
               command = self.master.quit,
               bd = 0,
               background = self.background,
               activebackground = self.backgroundActive,
               foreground = self.foreground,
               activeforeground = self.foregroundActive,
               ).pack()

    # action functions
    def add_inf(self):
        '''Function create new window where user can
        put his values
        '''
        # create window
        self.add_window = Tk()
        # set colors
        self.add_window.configure(bg = self.backgroundApp)
        Label(self.add_window,
              text = 'Currency',
              bd = 0,
              background = self.backgroundApp,
              foreground = self.background,
              font = 11,
              ).grid(row = 0, column = 0)
        Label(self.add_window,
              text = 'Numerues',
              bd = 0,
              background = self.backgroundApp,
              foreground = self.background,
              font = 11,
              ).grid(row = 0, column = 1)
        Button(self.add_window,
               text = 'Add',
               background = self.background,
               activebackground = self.backgroundActive,
               foreground = self.foreground,
               activeforeground = self.foregroundActive,
               font = 11,
               bd = 0).grid(row = 0, column = 2)
        # TODO: add options to select currency
        self.entry_add_inf = Entry(self.add_window,
                                   background = self.background,
                                   foreground = self.foreground,
                                   font = 11,
                                   bd = 0).grid(row = 1, column = 1)
        # TODO: write `Close` button in 1, 2 position of grid

    def shut_up_pc(self):
        print('Your PC already shut down')

    def load_colors():
        '''Colors are import from colors.json.
        If you whant change colors of gui
        change colors in this file
        '''
        with open('colors.json', 'r') as f:
            data = json_load(f)
        return tuple(data.items())
    
    def create_colors(self, colors = load_colors()):
        '''Function create colors in __init__()
        ============================================
        Arg --> colors from ('background', '#75642')
        make `self.background = '#75642'`
        '''
        for i in colors:
            exec('self.{} = "{}"'.format(i[0], i[1]))


if __name__ == '__main__':
    root = Tk()
    gui = CurViewGui(root)
    root.mainloop()
