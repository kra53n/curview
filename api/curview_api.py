'''Api of Curview
Goal --> make easy requests from gui
'''


### FUNCTIONS
def list_curs_name_gui():
    '''This funcion return tuple of curs with their names
    '''
    from api.parsing import CUR_PARS
    names = []
    for i in CUR_PARS:
        names.append(i[0])
    return names
