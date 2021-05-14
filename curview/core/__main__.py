from yaml_parser import cur_names_get
from yaml_parser import cur_inf_load

from web_parser import course_parse

from data import cur_expand


def cur_parse(path, filename, curname):
    """
    Parse information about currency.
    Return currency name, course of cur and type of cur as dict
    """
    # get from yaml information about parsing of currenct currency
    to_parse = cur_inf_load(path, filename, curname)

    # parse currency and get course of it
    course = course_parse(
        to_parse["url"],
        to_parse["tag"],
        to_parse["catch"],
        to_parse["signs"],
    )

    if to_parse["type"] != "crypto_cur":
        cur = cur_expand(
            curname,
            to_parse["type"],
            course,
        )
    if to_parse["type"] == "crypto_cur":
        dollar_parse = cur_inf_load(path, filename, "dollar")
        cur = cur_expand(
            curname,
            to_parse["type"],
            course,
            course_parse(
                dollar_parse["url"],
                dollar_parse["tag"],
                dollar_parse["catch"],
                dollar_parse["signs"],
            ),
        )
    return cur


if __name__ == "__main__":
    from random import choice
    path = "configs"
    filename = "parse.yaml"
    curname = choice(cur_names_get(path, filename))

    cur = cur_parse(path, filename, curname)
    print(cur)
