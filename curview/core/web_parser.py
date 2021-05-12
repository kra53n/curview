from bs4 import BeautifulSoup
import requests

from sys import exit


def get_html(url):
    """
    Function get html code and put it as text
    """
    try:
        html_doc = requests.get(url)
    except:
        print('\nCheck your connection!'.upper())
        input()
        exit()
    if html_doc.status_code != 200:
        print('Page have some problems!')
    return html_doc.text

def get_soup(url):
    soup = BeautifulSoup(get_html(url), 'html.parser')
    return soup

def delete_signs(value):
    '''Function check signs in value of currency
    after parsing'''
    if ' ' in value:
        value = value.replace(' ', '')
    if ',' in value:
        value = value.replace(',', '.')
    return value

def course_parser(url, search_tag, eq_count, signs = 'n'):
    '''Function that parse course of different
    currency'''
    soup = get_soup(url)
    count = 0
    for tag in soup.find_all(search_tag):
        count += 1
        if count == eq_count:
            currency = tag.string
            if signs.lower() == 'y':
                currency = delete_signs(currency)
    return float(currency)


# def exec_parsing(cur_pars):
#     mes_return = ''
#     for i in CUR_PARS:
#         if i[0] != CUR_PARS[0][0]:
#             mes_return += ', {}'.format(i[0])
#         else:
#             mes_return += CUR_PARS[0][0]
#         exec('{} = course_parser{}'.format(i[0], i[1:]))
#     return eval(mes_return)


if __name__ == "__main__":
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
