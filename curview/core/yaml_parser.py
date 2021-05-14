from yaml import safe_load
import os.path


def load_yaml(path, filename):
    with open(os.path.join(path, filename)) as f:
        return safe_load(f)

def curs_all_inf_load(path, filename):
    """
    From yaml extract all information about currencies
    for webscraping
    """
    data = load_yaml(path, filename)
    data = data["curs"]
    return data

def cur_inf_load(path, filename, curname):
    """
    If name is curname then return values
    """
    curs = curs_all_inf_load(path, filename)
    for el in curs:
        if el["name"] == curname:
            return el

def cur_names_get(path, filename):
    data = curs_all_inf_load(path, filename)
    return [i["name"] for i in data]
