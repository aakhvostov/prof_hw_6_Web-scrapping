import requests
from bs4 import BeautifulSoup


def page_parser():
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    for page in range(1, 2):
        URL = f'https://habr.com/ru/all/page{page}/'
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        li = soup.find('div', class_='layout__cell layout__cell_body'
                       ).find('section', class_='column-wrapper'
                              ).find('div', class_='posts_list'
                                     ).find('ul', class_='content-list content-list_posts shortcuts_items'
                                            ).find_all('li')

        for word in KEYWORDS:
            for article in li:
                try:
                    title_status = article.find('h2', class_='post__title')
                    title = title_status.text.strip()
                    link = title_status.find('a').get("href")
                    data = article.find('span', class_='post__time').text.strip()
                    content = article.find('div', class_='post__body post__body_crop'
                                           ).find('div', class_='post__text').text.strip()
                    if word in content.lower() or word in title.lower():
                        print(f'Ключевое слово "{word}" найдено в превью:\n{data}\n{title}\n{link}\n')
                except AttributeError:
                    pass


if __name__ == '__main__':
    page_parser()
