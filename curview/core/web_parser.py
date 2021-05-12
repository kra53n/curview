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
    """
    Function check signs in value of currency
    after parsing
    """
    if ' ' in value:
        value = value.replace(' ', '')
    if ',' in value:
        value = value.replace(',', '.')
    return value

def course_parse(url, search_tag, eq_count, signs = 'n'):
    """
    Parse course of currency
    """
    soup = get_soup(url)
    count = 0
    for tag in soup.find_all(search_tag):
        count += 1
        if count == eq_count:
            currency = tag.string
            if signs.lower() == 'y':
                currency = delete_signs(currency)
    return float(currency)



if __name__ == "__main__":
    from yaml_parser import curs_all_inf_load
    path = "../configs"
    filename = "parse.yaml"
    data = curs_all_inf_load(path, filename)
    print(data)
    print("========================================")

    for i in data:
        print(
            i["name"],
            "\t\t\t\t",
            course_parse(
                i["url"],
                i["tag"],
                i["catch"],
                i["signs"],
            ),
            "\t\t\t\t",
            i["type"],
        )
