# author: Krai53n
# date: 11.10.20

from os import system as sys
from time import sleep
from modules.clear import clear


### CONSTANTS
OPTIONS_TO_SELECT = '''
0 - quit
1 - show courses
2 - write currency
'''


### FUNCTIONS
def __greeting():
    '''Function print greeting
    '''
    clear()
    text = '''
    //   ) )
   //                  __             ( )  ___
  //        //   / / //  ) ) ||  / / / / //___) ) //  / /  / / 
 //        //   / / //       || / / / / //       //  / /  / /
((____/ / ((___( ( //        ||/ / / / ((____   ((__( (__/ /


'''
    for i in range(len(text)):
        print(text[i], end = '')
        sleep(0.001)

def __integer_agerssive():
    '''Function likes only integer numbers
    '''
    clear()
    print('Please type only integer numbers'.upper(), end = '')
    input()
    return -1


def instructer():
    '''Functin show greeting and options for select
    Then output in integer number as choice
    '''
    try:
        print(OPTIONS_TO_SELECT)
        choice = int(input('Your choice --> '))
    except:
        choice = __integer_agerssive()
    return choice

def show_courses():
    '''Function show courses of currency
    '''
    # TODO: numbers that have 0 after dot send to int
    import data
    clear()
    for i in range(1, 7):
        dic = data.typle_to_dict(data.options(i))
        text = 'Name: ' + dic['name']
        if 'course_rub' in dic.keys():
            text += '\t Course rub: {}'.format(round(dic['course_rub'], 2))
        if 'course_dlr' in dic.keys():
            text += '\tCourse dlr: {}'.format(round(dic['course_dlr'], 2))
        print(text)
    input()

def inf_write_currency():
    '''Function print iformation of options
    '''
    print('''What currency you whant to write?

    1 - dollar
    2 - bitcoin
    3 - ethereum
    4 - gold
    5 - silver
    6 - palladium
    ''')

def transit_data_to_sql3(data):
    '''Funtcion takes argument(dic) from write_currency()
    and transit this to base data with help of sqlite3
    '''
    import sqlite3 as sql
    keys = ('date', 'name', 'course_rub', 'rub', 'course_dlr', 'dlr')
    for key in keys:
        if key in data.keys():
            # TODO: finish this
            print('All is work!', data[key])
        input()

def write_currency():
    '''Function write kind of currency to file
    '''
    import data
    clear()
    inf_write_currency()
    option = input('Write your option --> ')
    # TODO: write what is it mean in under
    dic = data.typle_to_dict(data.options(option, 1))
    print(dic)
    input()
    transit_data_to_sql3(dic)


if __name__ == '__main__':
    __greeting()
    sleep(1.5)
    clear()
    choice = None
    while choice != 0:
        choice = instructer()
        if choice > -1 and choice < 3:
            if choice == 1:
                show_courses()
            elif choice == 2:
                write_currency()
        else:
            clear()
            print('You can type only numbers in options'.upper(), end = ' ')
            input()
        clear()
