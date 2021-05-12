"""
from yaml_parser import curs_all_inf_load
path = "../configs"
filename = "parse.yaml"
data = curs_all_inf_load(path, filename)

for i in data:
    print(
        i["name"],
        "\t\t",
        course_parser(
            i["url"],
            i["tag"],
            i["catch"],
            i["signs"],
        ),
        "\t\t",
        i["type"],
    )
"""

def curs_info(curname, data_to_parse):
    """
    Argument      | Description
    --------------------------------
    curname       | name of currency
    data_to_parse | data to parse
    """
    pass
