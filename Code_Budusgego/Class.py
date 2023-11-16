import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    # Отправка HTTP-запроса на заданный URL
    response = requests.get(url)

    # Проверка успешности запроса
    if response.status_code == 200:
        # Использование BeautifulSoup для извлечения содержимого тега <title>
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return title

    return None


# Пример использования
url = 'https://example.org'
title = fetch_title(url)
if title:
    print(f"Заголовок страницы {url}: {title}")
else:
    print(f"Не удалось получить заголовок страницы {url}.")