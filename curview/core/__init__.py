from yaml_parser import cur_names_get
from date import date
from wwdb import wwdb

from yaml_parser import cur_inf_load as __cur_inf_load
from web_parser import course_parse as __course_parse
from data import cur_expand as __cur_expand


def cur_parse(path, filename, curname):
    """
    Parse information about currency.
    Return currency name, course of cur and type of cur as dict
    """
    # get from yaml information about parsing of currenct currency
    to_parse = __cur_inf_load(path, filename, curname)

    # parse currency and get course of it
    course = __course_parse(
        to_parse["url"],
        to_parse["tag"],
        to_parse["catch"],
        to_parse["signs"],
    )

    if to_parse["type"] != "crypto_cur":
        cur = __cur_expand(
            curname,
            to_parse["type"],
            course,
        )
    if to_parse["type"] == "crypto_cur":
        dollar_parse = __cur_inf_load(path, filename, "dollar")
        cur = __cur_expand(
            curname,
            to_parse["type"],
            course,
            __course_parse(
                dollar_parse["url"],
                dollar_parse["tag"],
                dollar_parse["catch"],
                dollar_parse["signs"],
            ),
        )
    return cur
