# # currencies that have difference btw other(bit and dlr)
# # other currency have less details
# CUR_ROW = (
#     'ethereum',
#     'bitcoin'
# )
# 
# 
# def list_curs_name():
#     '''
#     Return tuple of currency names
#     '''
#     from .parsing import CUR_PARS
#     return [i[0] for i in CUR_PARS]
# 
# def cur_put_db(cur, amount = 0):
#     '''Put currenct to data base
#     Argument cur is type of currency
#     '''
#     from .data import cur_to_dict
#     from .wwdb import wwdb
#     data = cur_to_dict(cur, amount)
#     # 0 mean that we write currency to db
#     wwdb(data, 0)


from parsing import exec_parsing

from yaml import safe_load
import os.path


def load_parsing_inf(path, filename):
    with open(os.path.join(path, filename)) as f:
        return safe_load(f)

def extract_curs():
    pass

def run_exec_parsing():
    """
    This function is something that help me to understand
    what`s happends here. In fututre I will delete this.
    """
    path, filename = "configs", "parsing.yaml"
    exec_parsing(load_parsing_inf(path, filename))


if __name__ == "__main__":
    print(load_parsing_inf("configs", "parsing.yaml"))
    #run_exec_parsing()
