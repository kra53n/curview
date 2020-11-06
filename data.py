from modules.parsing import dollar, bitcoin, ethereum, gold, silver, palladium
from modules.clear import clear as __clear


### FUNCTIONS
def __ask(ask):
    '''Function ask user about something
    '''
    return input(ask)

def __try_again():
    '''Function asks user type one more time
    beacause user type someting uncorrectly
    '''
    __clear()
    input('I`m sorry bit you type something strange! ')
    input('Let`s try again! ')

def __dollar(ask):
    '''Function which will work if we choose dollar
    function return course of dollar in rubles and
    our money in rubles
    '''
    if ask == 1:
        num = __ask('How many dollars you have? --> ')
    try:
        if ask == 1:
            num = float(num)
        else:
            num = 0
        course_dollar_rub = dollar
        dollar_rub = course_dollar_rub * num
        return course_dollar_rub, dollar_rub
    except ValueError:
        __try_again()

def __bitcoin(ask):
    '''Function which will work if we choose bictcoin
    function return course of btc in dollars, course btc in rub,
    our money in dollars and our money in rubles
    '''
    if ask == 1:
        num = __ask('How many bitcoins you have --> ')
    try:
        if ask == 1:
            num = float(num)
        else:
            num = 0
        course_btc_dollar = bitcoin
        course_btc_rub = course_btc_dollar * dollar
        btc_dollars = course_btc_dollar * num
        btc_rubles = course_btc_rub * num
        return course_btc_dollar, course_btc_rub, btc_dollars, btc_rubles
    except ValueError:
        __try_again()

def __ethereum(ask):
    '''Function which will work if we choose bictcoin
    function return course of btc in dollars, course btc in rub,
    our money in dollars and our money in rubles
    '''
    if ask == 1:
        num = __ask('How many ethereum you have --> ')
    try:
        if ask == 1:
            num = float(num)
        else:
            num = 0
        course_eth_dollar = ethereum
        course_eth_rub = course_eth_dollar * dollar
        eth_dollars = course_eth_dollar * num
        eth_rubles = course_eth_rub * num
        return course_eth_dollar, course_eth_rub, eth_dollars, eth_rubles
    except ValueError:
        __try_again()


def __gold(ask):
    '''Function which will work if you choose gold in option
    function return course of gold in rubles and our money in rub
    '''
    if ask == 1:
        num = __ask('How many gold you have --> ')
    try:
        if ask == 1:
            num = float(num)
        else:
            num = 0
        course_gold_rubles = gold
        gold_rubles = course_gold_rubles * num
        return course_gold_rubles, gold_rubles
    except ValueError:
        __try_again()

def __silver(ask):
    '''Function which will work if you choose silver
    in option
    function return course of silver in rub and our money in rub
    '''
    if ask == 1:
        num = __ask('How many silver you have --> ')
    try:
        if ask == 1:
            num = float(num)
        else:
            num = 0
        course_silver_rubles = silver
        silver_rubles = course_silver_rubles * num
        return course_silver_rubles, silver_rubles
    except:
        __try_again()

def __palladium(ask):
    '''Function which will work if we choose
    option 6(palladium)
    function return course of palladium in rub and our money in run
    '''
    if ask == 1:
        num = __ask('How many palladium you have --> ')
    try:
        if ask == 1:
            num = float(num)
        else:
            num = 0
        course_palladium_rubles = palladium
        palladium_rubles = course_palladium_rubles * num
        return course_palladium_rubles, palladium_rubles
    except:
        __try_again()

def __exec_option(option, ask):
    # TODO write comment to function
    '''Function that
    '''
    if option == 1:
        name = 'dollar'
        course_rub, rub = __dollar(ask)
    if option == 2:
        name = 'bitcoin'
        course_dlr, course_rub, dlr, rub = __bitcoin(ask)
    if option == 3:
        name = 'ethereum'
        course_dlr, course_rub, dlr, rub = __ethereum(ask)
    if option == 4:
        name = 'gold'
        course_rub, rub = __gold(ask)
    if option == 5:
        name = 'silver'
        course_rub, rub = __silver(ask)
    if option == 6:
        name = 'palladium'
        course_rub, rub = __palladium(ask)
    try:
        if option == 2 or option == 3:
            return name, course_dlr, course_rub, dlr, rub
        else:
            return name, course_rub, rub
    except:
        pass

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
    from modules.date import date
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
