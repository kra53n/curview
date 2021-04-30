"""
Stylize tkinter widgets
"""


from tkinter import Button


class ButtonMenu(Button):
    '''Set default Button from tkinter our settings
    for menu
    '''
    def __init__(self, *args, **kwargs):
        # TODO: delete all colors under
        self.backgroundapp =  "#2C3531"
        self.background = "#D1E8E2"
        self.backgroundactive = "#116466"
        self.foreground = "#116466"
        self.foregroundactive = "#D1E8E2"

        super().__init__(
            *args,
            **kwargs,
            background = self.background,
            activebackground = self.backgroundactive,
            foreground = self.foreground,
            activeforeground = self.foregroundactive,
            bd = 0,
        )
