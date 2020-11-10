import requests
from bs4 import BeautifulSoup


def post_parser():
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    for page in range(1, 2):
        URL = f'https://habr.com/ru/all/page{page}/'
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        for article in soup.find_all('article', class_='post'):
            post_url = article.find('a', class_='post__title_link') # нашли в превьюшке ссылку на пост
            response_post = requests.get(post_url.attrs.get('href'))
            soup_post = BeautifulSoup(response_post.text, 'html.parser')
            post_text = soup_post.find('article', class_='post post_full')
            for word in KEYWORDS:
                if word in post_text.text.strip():
                    title = post_text.find('span', class_='post__title-text').text.strip()
                    data = post_text.find('span', class_='post__time').text.strip()
                    print(f'Ключевое слово "{word}" найдено в статье:\n{data}\n{title}\n{post_url.attrs.get("href")}\n')


if __name__ == '__main__':
    post_parser()
