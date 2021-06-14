from tkinter import Frame

from .style import colors
from .style import ButtonMenu


class Menu(Frame):
    def __init__(self, main, options_and_commands, colors=colors):
        """
        + --------------------------- ARGUMENTS ------------------------ +
        | options_and_commands - tuple or list that consider another     |
        |                        tuple or list that consider name of     |
        |                        option and action of option             |
        + -------------------------------------------------------------- +
        """
        self.main = main
        self.options_and_commands = options_and_commands
        Frame.__init__(self, self.main)

        self.main.config(bg=colors["foreground"])

        self.__init_options()

    def __init_options(self):
        for option_and_command in self.options_and_commands:
            ButtonMenu(
                text=option_and_command[0].capitalize(),
                command=option_and_command[1],
            ).pack(fill="x", padx=3, pady=3)
