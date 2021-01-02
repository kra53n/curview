from bs4 import BeautifulSoup
import requests
from sys import exit


### CONSTANTS
PATH_SITE = 'https://форум-трейдеров.рф/chart-online.php'
PATH_SITE_CRYPTO = 'https://www.banknn.ru/kurs-kriptovalyut'
PATH_SITE_METAL = 'https://cbr.ru/hd_base/metall/metall_base_new/'
CUR_PARS = (
        ('dollar', PATH_SITE, 'span', 11),
        ('bitcoin', PATH_SITE_CRYPTO, 'td', 4, 'y'),
        ('ethereum', PATH_SITE_CRYPTO, 'td', 9, 'y'),
        ('gold', PATH_SITE_METAL, 'td', 2, 'y'),
        ('silver', PATH_SITE_METAL, 'td', 3, 'y'),
        ('palladium', PATH_SITE_METAL, 'td', 5, 'y')
)


### FUNCTIONS
def get_html(url = PATH_SITE):
    '''Function get html code and put it as text
    '''
    try:
        html_doc = requests.get(url)
    except:
        print('\nCheck your connection!'.upper())
        input()
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
'''Output everything what we have in CUR_PARS
'''
for i in CUR_PARS:
    exec('{} = course_parser{}'.format(i[0], i[1:]))
