from bs4 import BeautifulSoup
import requests
from sys import exit
from clear import clear


### CONSTANTS
PATH_SITE = 'https://форум-трейдеров.рф/chart-online.php'
PATH_SITE_CRYPTO = 'https://www.banknn.ru/kurs-kriptovalyut'
PATH_SITE_METAL = 'https://cbr.ru/hd_base/metall/metall_base_new/'


### FUNCTIONS
def get_html(url = PATH_SITE):
    '''Function get html code and put it as text
    '''
    try:
        html_doc = requests.get(url)
    except:
        print()
        print('Check your connection!'.upper())
        input()
        clear()
        exit()
    if html_doc.status_code != 200:
        print('Page have some problems!')
    return html_doc.text

def get_soup(url = PATH_SITE):
    soup = BeautifulSoup(get_html(url), 'html.parser')
    return soup

def check_signs(value):
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
                currency = check_signs(currency)
    return float(currency)


### OUTPUT
dollar = course_parser(PATH_SITE, 'span', 11)
bitcoin = course_parser(PATH_SITE_CRYPTO, 'td', 4, 'y')
ethereum = course_parser(PATH_SITE_CRYPTO, 'td', 9, 'y')
gold = course_parser(PATH_SITE_METAL, 'td', 2, 'y')
silver = course_parser(PATH_SITE_METAL, 'td', 3, 'y')
palladium = course_parser(PATH_SITE_METAL, 'td', 5, 'y')