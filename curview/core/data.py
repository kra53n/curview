from .parsing import CUR_PARS, exec_parsing
from .clear import clear
from .constants import CUR_ROW
from .date import date


### INITIALIZE CURRENCY
cur_vals =  exec_parsing()
for i in range(len(CUR_PARS)):
    exec('{} = {}'.format(CUR_PARS[i][0], cur_vals[i]))


### FUNCTIONS
def cur_to_dict(cur, amount = 0):
    '''Function create dict with full information of currency
    '''
    data = {'date': date,
            'name': cur,
            'amount': amount,
            }
    if cur in CUR_ROW:
        data['course_dlr'] = eval(cur)
        data['dlr'] = eval(cur) * amount
        data['course_rub'] = round((eval(cur) * dollar), 4)
        data['rub'] = round((eval(cur) * dollar * amount), 4)
    if cur not in CUR_ROW:
        data['course_rub'] = round(eval(cur), 4)
        data['rub'] = round(eval(cur) * amount, 4)
    return data
