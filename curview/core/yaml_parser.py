from yaml import safe_load
import os.path


def load_yaml(path, filename):
    with open(os.path.join(path, filename)) as f:
        return safe_load(f)

def curs_all_inf_extract(path, filename):
    """
    From yaml file extract currencies
    """
    data = load_yaml(path, filename)
    data = data["curs"]
    return data

def cur_names_extract(path, filename):
    data = curs_all_inf_extract(path, filename)
    return [tuple(name.keys())[0] for name in data]


if __name__ == "__main__":
    path = "../configs"
    filename = "parsing.yaml"

    #print(curs_all_inf_extract(path, filename))
    print(cur_names_extract(path, filename))
