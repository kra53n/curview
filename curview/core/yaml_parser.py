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

def cur_names_get(path, filename):
    data = curs_all_inf_load(path, filename)
    return [i["name"] for i in data]


if __name__ == "__main__":
    path = "../configs"
    filename = "parsing.yaml"

    data = curs_all_inf_load(path, filename)
    [print(i) for i in data]
    print(cur_names_get(path, filename))
