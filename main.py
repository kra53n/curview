from os import system as sys
from time import sleep
from clear import clear
from wwdb import wwdb
from constants import CUR_CHOOSE_TEXT


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
    print(f'What currency you whant to write?\n{CUR_CHOOSE_TEXT}')

def write_currency(choice):
    '''Function write kind of currency to file
    '''
    import data
    clear()
    inf_write_currency()
    option = input('Write your option --> ')
    dic = data.typle_to_dict(data.options(option, 1))
    wwdb(dic, choice)


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
                write_currency(0)
        else:
            clear()
            print('You can type only numbers in options'.upper(), end = ' ')
            input()
        clear()
