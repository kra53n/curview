from tkinter import Tk, Button
from json import load as json_load


class CurViewGui:
    def __init__(self, master):
        ### GENERATION OF USER INTERFACE
        self.create_colors()
        self.master = master
        # identify width
        self.width = master.winfo_screenwidth()
        # give title
        if self.width > 400:
            master.title('CurView - Currency view')
        else:
            master.title('CurView')
        master.configure(background = self.background)
        # create widgets
        self.create_widgets()

    def create_widgets(self):
        print('Widgets are create')
        Button(self.master,
               text = 'Shut up PC',
               command = self.shut_up_pc,
               bd = 0,
               background = self.background_elem_not_act,
               activebackground = self.background_elem_act,
               foreground = self.foreground_elem_non_act,
               activeforeground = self.foreground_elem_act,
               ).pack()
        Button(self.master,
               text = 'Quit',
               command = self.master.quit,
               bd = 0,
               background = self.background_elem_not_act,
               activebackground = self.background_elem_act,
               foreground = self.foreground_elem_non_act,
               activeforeground = self.foreground_elem_act,
               ).pack()

    def shut_up_pc(self):
        print('Your PC already shut down')

    def load_colors():
        '''Colors are import from colors.json.
        If you whant change colors of gui
        change colors in this file
        '''
        # TODO: rewrite comment of funtion
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
