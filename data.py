from parsing import dollar, bitcoin, ethereum, gold, silver, palladium
from clear import clear


### FUNCTIONS
def __try_again():
    '''Function asks user type one more time
    beacause user type someting uncorrectly
    '''
    clear()
    input('I`m sorry but you type something strange! ')
    input('Let`s try again! ')

def __distrebute_currency(ask, cur):
    ''' Function distrebute currunecy on what we need
    for example we need in ifnormation of dlr, rub
    and e.t.c.
    =====================================================
    Args:
        ask:
            ask = 0 --> we don`t need in numerous of cur
            ask = 1 --> we need in numeriys if cur
        cur --> type of currency
    '''
    num = 0
    row = ('bitcoin', 'ethereum')
    if ask == 1:
        num = float(input(f'How many {cur} you have --> '))
    course_rub = eval(cur)
    rub = course_rub * num
    if cur in row:
        course_dlr = eval(cur)
        course_rub = course_dlr * dollar
        dlr = course_dlr * num
        rub = course_rub * num
        return course_dlr, course_rub, dlr, rub
    else:
        return course_rub, rub

def __exec_option(option, ask):
    '''Function translate type of currency to __destrebute_currence
    '''
    curs = ('dollar', 'bitcoin', 'ethereum', 'gold', 'silver', 'palladium')
    row = ('bitcoin', 'ethereum')
    for i in range(1, 7):
        if i == option:
            name = curs[i-1]
            if name in row:
                course_dlr, course_rub, dlr, rub = __distrebute_currency(ask,
                                                                         name)
            else:
                course_rub, rub = __distrebute_currency(ask, name)
    if name in row:
        return name, course_dlr, course_rub, dlr, rub
    else:
        return name, course_rub, rub

def options(option = None, ask = 0):
    '''Function ask which value you whant pass
    function return typle with data of __exec_option()
    '''
    text = '''
    CHOOSE THE OPTION
    0 - exit
    1 - dollar
    2 - bitcoin
    3 - ethereum
    4 - gold
    5 - silver
    6 - palladium

Type your option --> '''
    while option != 0:
        if option == None:
            option = input(text)
            ask = 1
        try:
            option = int(option)
            if option > 6 or option < 0:
                __try_again()
                continue
        except ValueError:
            __try_again()
            continue
        data = tuple(__exec_option(option, ask))
        return data

def typle_to_dict(data_typle):
    '''Function have argumnet d a t a _ t y p l e
    this argument define the length and with help of this
    processing it to dictionary
    example --> typle_do_dict(options())
    '''
    from date import date
    data = {'date': date}
    if len(data_typle) == 3:
        # dollarm gold, sivler, palladium
        # name, course_rub, rub
        titles = ('name', 'course_rub', 'rub')
        for i in range(len(data_typle)):
            data[titles[i]] = data_typle[i]
    if len(data_typle) == 5:
        # bitcoin, ethereum
        # name, course_dlr, course_rub, dlr, rub
        titles = ('name', 'course_dlr', 'course_rub', 'dlr', 'rub')
        for i in range(len(data_typle)):
            data[titles[i]] = data_typle[i]
    return data