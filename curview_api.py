'''Api of Curview
Goal --> make easy requests from gui
'''


### FUNCTIONS
def list_curs_name():
    '''This funcion return tuple of curs with their names
    '''
    from api.parsing import CUR_PARS
    return [i[0] for i in CUR_PARS]

def cur_put_db(cur, amount = 0):
    '''Put currenct to data base
    Argument cur is type of currency
    '''
    from api.data import cur_to_dict
    from api.wwdb import wwdb
    data = cur_to_dict(cur, amount)
    # 0 mean that we write currency to db
    wwdb(data, 0)
