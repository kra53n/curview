'''Api of Curview
Goal --> make easy requests from gui
'''


### FUNCTIONS
def list_curs_name():
    '''This funcion return tuple of curs with their names
    '''
    from api.parsing import CUR_PARS
    return [i[0] for i in CUR_PARS]
