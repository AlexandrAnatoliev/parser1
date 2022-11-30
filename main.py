# parser 1

# Парсим анекдоты с сайта
# Видео в You Tube от Хауди-Хо "Парсинг в Python за 10 минут!"

import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://anekdoty.ru/samye-smeshnye/")
html = BS(r.content, 'html.parser')

# Выводит все анекдоты со страницы (с мусором)
fun = html.select(" div > div.holder-body > p")
print(fun)
