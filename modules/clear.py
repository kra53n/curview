# author: Krai53n
# date: 15.10.20

from os import system
from sys import platform


def clear():
    '''Function clear what was before in
    terminal and aslo check our OS'''
    if  platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        system('clear')
    if platform == 'win32':
        system('cls')