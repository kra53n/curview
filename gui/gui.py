from tkinter import Tk, Button


class CurViewGui:
    def __init__(self, master):
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


if __name__ == '__main__':
    root = Tk()
    gui = CurViewGui(root)
    root.mainloop()
