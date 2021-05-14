from yaml_parser import cur_names_get
from yaml_parser import cur_inf_load

from web_parser import course_parse


def cur_parse(path, filename, curname):
    """
    Parse information about currency.
    Return currency name, course of cur and type of cur as dict
    """
    to_parse = cur_inf_load(path, filename, curname)

    cur = course_parse(
        to_parse["url"],
        to_parse["tag"],
        to_parse["catch"],
        to_parse["signs"],
    )
    return {
        "name": to_parse["name"],
        "course": cur,
        "type": to_parse["type"],
    }


if __name__ == "__main__":
    from random import choice
    path = "configs"
    filename = "parse.yaml"
    curname = choice(cur_names_get(path, filename))

    cur = cur_parse(path, filename, curname)
    print(cur)
