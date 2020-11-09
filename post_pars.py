import requests
from bs4 import BeautifulSoup


def post_parser():
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    for page in range(1, 2):
        URL = f'https://habr.com/ru/all/page{page}/'
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        for article in soup.find_all('article', class_='post'):
            post_url = article.find('a', class_='post__title_link')
            response_post = requests.get(post_url.attrs.get('href'))
            soup_post = BeautifulSoup(response_post.text, 'html.parser')
            for art in soup_post.find_all('article', class_='post'):
                hubs = art.find_all('a', class_='hub-link')
                hubs_text = list(map(lambda x: x.text.lower(), hubs))
                for word in KEYWORDS:
                    if word in hubs_text:
                        title_element = art.find('span', class_='post__title-text')
                        title = title_element.text
                        data = art.find('span', class_='post__time')
                        print(f'{data.text}, {title} - {post_url.attrs.get("href")}')


if __name__ == '__main__':
    post_parser()
