import requests
from bs4 import BeautifulSoup


def page_parser():
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    for page in range(1, 5):
        URL = f'https://habr.com/ru/all/page{page}/'
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup.find('article', class_='post')
        for article in soup.find_all('article', class_='post'):
            hubs = article.find_all('a', class_='hub-link')
            hubs_text = list(map(lambda x: x.text.lower(), hubs))
            for word in KEYWORDS:
                if word in hubs_text:
                    title_element = article.find('a', class_='post__title_link')
                    title = title_element.text
                    link = title_element.attrs.get('href')
                    data = article.find('span', class_='post__time')
                    print(f'{data.text}, {title} - {link}')


if __name__ == '__main__':
    page_parser()
