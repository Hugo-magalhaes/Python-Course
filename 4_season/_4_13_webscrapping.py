# type:ignore
# -m http.server -d site.py/ 3333
# ! O valor final é a porta do server http
#  http:// --> 80
#  https:// --> 443
# -- python -m http.server -d origem_pasta_site\ porta

import re

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)


# print(response.status_code)
# print(response.headers)

# print(response.json())  # ! Só funciona com api
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')


# if parsed_html.title.text is not None:
#     print(parsed_html.title.text)


top_jobs = parsed_html.select_one('#intro > div > div > article > h2')

article = top_jobs.parent

# print(top_jobs.text)

# print(top_jobs.parent.text)

for p in article.select('p'):
    print(re.sub(r'\s{1,}', ' ', p.text).strip())
