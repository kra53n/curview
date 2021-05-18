"""
The style of differant elements in the app.
"""

from yaml import safe_load
import os.path

from tkinter import Button
from tkinter import Label


def colors_yaml_load(path, filename):
    """
    Parse colors.yaml and return as dict(name: color code).
    For example: "background": "#777777"
    """
    with open(os.path.join(path, filename)) as f:
        return safe_load(f)

colors = colors_yaml_load("configs", "colors.yaml")


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
