"""
Stylize tkinter widgets
"""


from tkinter import Button


class ButtonMenu(Button):
    '''Set default Button from tkinter our settings
    for menu
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            background = BACKGROUND,
            activebackground = BACKGROUNDACTIVE,
            foreground = FOREGROUND,
            activeforeground = FOREGROUNDACTIVE,
            bd = 0,
        )
