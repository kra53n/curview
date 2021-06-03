# WWDB - WORK WITH DATA BASE

import sqlite3 as sql


def text_for_creating_table(currency):
    message = 'CREATE TABLE IF NOT EXISTS `{}` '.format(currency["name"])
    message += '(`date` STRING, `amount` REAL,`course_rubles` REAL, '
    message += '`rubles` REAL'
    if currency["cur_type"] == "crypto_cur":
        message += ', `course_dollar` REAL, `dollar` REAL'
    message += ')'
    return message

def text_for_filling_table(currency, date, amount):
    """
    Function collect message in dependence of
    situation
    ================================================
    Argument of currency get dic of currency with
    information
    """
    message = 'INSERT INTO `{}` '.format(currency['name'])
    message += 'VALUES ("{}", '.format(date)
    message += '{}, '.format(amount)
    message += '{}, {}'.format(
        currency['course_ruble'],
        currency['course_ruble'] * amount,
    )
    if currency["cur_type"] == "crypto_cur":
        message += ', {}, {}'.format(
            currency["course_dollar"],
            currency["course_dollar"] * amount,
        )
    message += ')'
    return message

def wwdb(db_name, db_choice, currency, amount, date):
    """
    Function write or recieve data from data base
    ================================================
    Argument currency get dic with inf of currency
    ================================================
    Argument choice:
        choice = "write"
        choice = "get"
    """
    con = sql.connect(db_name)
    message = text_for_creating_table(currency)
    with con:
        cur = con.cursor()
        # creating table if not exists
        cur.execute(message)
        if db_choice == "write":
            cur.execute(text_for_filling_table(currency, date, amount))
        elif db_choice == "get":
            # TODO: put it to a seperate function
            cur.execute('SELECT * FROM `{}`'.format(currency['name']))
            names = list(map(lambda x: x[0], cur.description))
            rows = cur.fetchall()
            return names, rows
        else:
            print('You are have mistake in choice'.upper())
        con.commit()
        cur.close()
