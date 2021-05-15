import time


### FUNCTIONS
def exactly_time():
    '''Function return tuple with this data:
    year, month and day
    '''
    # request our date in seconds
    ticks = time.time()
    # convert ticks in set
    localtime = time.localtime(ticks)
    # convert localtime(set) in tuplre
    localtime = tuple(localtime)
    # we do some kind of this 25.08.20
    return localtime

def get_date_inf(kind, ex_t = exactly_time()):
    '''Function return year, month and day
    parametre kind have value 0(year), 1(month), 2(day)
    '''
    inf = str(ex_t[kind])
    if kind == 0:
        inf = inf[-2:]
    if kind == 1 or kind == 2:
        if ('0' not in inf) and (len(inf) == 1):
            inf = '0' + inf
    return inf
    

def date():
    return get_date_inf(2) + '.' + get_date_inf(1) + '.' + get_date_inf(0)
