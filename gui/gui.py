from tkinter import Tk, Button
from json import load as json_load


class CurViewGui:
    def __init__(self, master):
        ### CONSTANTS
        COLORS_ELEMS = ('background')
        ### BUILD
        self.master = master
        # identify width
        self.width = master.winfo_screenwidth()
        # give title
        if self.width > 400:
            master.title('CurView - Currency view')
        else:
            master.title('CurView')
        # create widgets
        self.create_widgets()
        print(self.background())

    def create_widgets(self):
        print('Widgets are create')
        Button(self.master,
               text = 'Shut up PC',
               command = self.shut_up_pc
               ).pack()
        Button(self.master,
               text = 'Quit',
               command = self.master.quit
        ).pack()

    def shut_up_pc(self):
        print('Your PC already shut down')

    def load_colors(self):
        '''Colors are import from colors.json.
        If you whant change colors of gui
        change colors in this file
        '''
        with open('colors.json', 'r') as f:
            data = json_load(f)
        self.background = data['background']
        # for elem in elems:
            # exec('self.{0} = data["{0}"]'.format(elem))
            # exec('self.background = data["background"]')


if __name__ == '__main__':
    root = Tk()
    gui = CurViewGui(root)
    root.mainloop()
