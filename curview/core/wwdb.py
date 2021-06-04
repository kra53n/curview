# wwdb - WORK WITH DATA BASE

import sqlite3 as sql


class Wwdb:
    # NOTE: some arguments could be better trasit to other place
    def __init__(self, db_name, currency, amount=None, date=None):
        """
        + ---------------------- ARGUMENTS --------------------- +
        | currency - dictionary with keys(`name`, `cur_type`,    |
        |            `course_ruble`, `course_dollar`             |
        + ------------------------------------------------------ +
        """
        self.currency = currency
        self.amount = amount
        self.date = date

        self.con = sql.connect(db_name)

    def __text_for_creating_table(self):
        message = 'CREATE TABLE IF NOT EXISTS `{}` '.format(
            self.currency["name"])
        message += '(`date` STRING, `amount` REAL,`course_rubles` REAL, '
        message += '`rubles` REAL'
        if self.currency["cur_type"] == "crypto_cur":
            message += ', `course_dollar` REAL, `dollar` REAL'
        message += ')'
        return message

    def __text_for_filling_table(self):
        """
        Function collect message in dependence of
        situation
        ================================================
        Argument of currency get dic of currency with
        information
        """
        message = 'INSERT INTO `{}` '.format(self.currency['name'])
        message += 'VALUES ("{}", '.format(self.date)
        message += '{}, '.format(self.amount)
        message += '{}, {}'.format(
            self.currency['course_ruble'],
            self.currency['course_ruble'] * self.amount,
        )
        if self.currency["cur_type"] == "crypto_cur":
            message += ', {}, {}'.format(
                self.currency["course_dollar"],
                self.currency["course_dollar"] * self.amount,
            )
        message += ')'
        return message

    def put(self):
        with self.con:
            cur = self.con.cursor()

            # message for creating table
            message = self.__text_for_creating_table()
            # creating table if not exists
            cur.execute(message)

            # put our curreny dictionary to database
            cur.execute(self.__text_for_filling_table())

            self.con.commit()
            cur.close()

    def get(self):
        """
        Function get infomation about currency from database

        Return list with tuples where 0 element is name of colums and
        other elements are data of this colums
        """
        with self.con:
            cur = self.con.cursor()

            # get information about currency from database
            cur.execute('SELECT * FROM `{}`'.format(currency['name']))

            names = list(map(lambda x: x[0], cur.description))
            rows = cur.fetchall()
            names_and_rows = list()
            names_and_rows.append(tuple(names))
            names_and_rows.extend(rows)

            self.con.commit()
            cur.close()

            return names_and_rows
