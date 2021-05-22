"""
The style of differant elements in the app.
"""

from tkinter import Button
from tkinter import Label
from tkinter import Entry

import os.path
from yaml import safe_load


# parse colors.yaml and return as dict(name: color code).
# for example: "background": "#777777"
with open(os.path.join("configs", "colors.yaml")) as f:
    colors = safe_load(f)


class ButtonMenu(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            background=colors["background"],
            activebackground=colors["activebackground"],
            foreground=colors["foreground"],
            activeforeground=colors["activeforeground"],
            bd=0,
        )


class LabelAddWindow(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            background=colors["backgroundapp"],
            foreground=colors["background"],
            bd=0,
        )


class ButtonAddWindow(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            background=colors["background"],
            activebackground=colors["backgroundapp"],
            foreground=colors["backgroundapp"],
            activeforeground=colors["background"],
            bd=0,
        )

class EntryAddWindow(Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            background=colors["background"],
            foreground=colors["backgroundapp"],
            bd=0,
        )
