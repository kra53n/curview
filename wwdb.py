# WWDB - WORK WITH DATA BASE

import sqlite3 as sql
from date import exactly_time as ex_t


### CONSTANTS
NAME_DB = str(ex_t()[0])


### FUNCTIOCNS
def write_to_db():
    pass

def wwdb(currency, choice):
    '''Function write or recieve data from data base
    ================================================
    Argument currency get type of currency
    ================================================
    Argument choice:
        choice = 0 or choice = 1
        choice = 0 --> write
        choice = 1 --> recieve
    '''
    con = sql.connect(NAME_DB)
    # TODO: finish message
    row = ['bitcoin', 'ethereum']
    message = 'CREATE TABLE IF NOT EXISTS `{}` '.format(currency)
    message += '`date` STRING, `course_rub` REAL, `rub`'
    if currency in row:
        message += '(`course_dlr` REAL, `dlr` REAL)'

    with con:
        cur = con.cursor()
        cur.execute(message)
