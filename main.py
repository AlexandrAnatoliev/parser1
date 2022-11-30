# parser 1

# Парсим анекдоты с сайта
# Видео в You Tube от Хауди-Хо "Парсинг в Python за 10 минут!"

import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://anekdoty.ru/samye-smeshnye/")
html = BS(r.content, 'html.parser')

# Скачиваем все анекдоты со страницы (с мусором)
fun = html.select(" div > div.holder-body > p")


# чистим текст строки и формируем анекдот
def clean_text(text):
    joke = str(text)
    if '<' in joke:
        joke = joke[:joke.find('<')] + joke[joke.find('>') + 1:]
    return joke


s = str(fun[0])
s = clean_text(s)
print(s)
