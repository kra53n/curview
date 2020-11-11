# WWDB - WORK WITH DATA BASE

import sqlite3 as sql
from date import exactly_time as ex_t


### CONSTANTS
NAME_DB = str(ex_t()[0]) + '.db'


### FUNCTIOCNS
def text_for_creating_table(currency):
    '''Funtcion collect message in dependence of
    situation
    ================================================
    Argument currency get type of currency for goal
    of function
    '''
    row = ['bitcoin', 'ethereum']
    message = 'CREATE TABLE IF NOT EXISTS `{}` '.format(currency)
    message += '(`date` STRING, `course_rubles` REAL, `rubles` REAL'
    if currency in row:
        message += ', `course_dollar` REAL, `dollar` REAL'
    message += ')'
    return message

def text_for_filling_table(currency):
    '''Function collect message in dependence of
    situation
    ================================================
    Argument of currency get dic of currency with
    information
    '''
    row = ['bitcoin', 'ethereum']
    message = 'INSERT INTO `{}` '.format(currency['name'])
    message += 'VALUES ("{}", '.format(currency['date'])
    message += '{}, {}'.format(currency['course_rub'], currency['rub'])
    if currency['name'] in row:
        message += ', {}, {}'.format(currency['course_dlr'], currency['dlr'])
    message += ')'
    return message

def wwdb(currency, choice):
    '''Function write or recieve data from data base
    ================================================
    Argument currency get dic with inf of currency
    ================================================
    Argument choice:
        choice = 0 or choice = 1
        choice = 0 --> write
        choice = 1 --> recieve
    '''
    con = sql.connect(NAME_DB)
    message = text_for_creating_table(currency['name'])
    with con:
        cur = con.cursor()
        # creating table if not exists
        cur.execute(message)
        if choice == 0:
            cur.execute(text_for_filling_table(currency))
        elif choice == 1:
            cur.execute('SELECT * FROM `{}`'.format(currency['name']))
            rows = cur.fetchall()
            for row in rows:
                for i in range(len(row)):
                    print(row[i], end = ' ')
        else:
            print('You are have mistake in choice'.upper())
        con.commit()
        cur.close()
