from requests import get, post
from pprint import pprint

print(post('http://localhost:5000/api/news', json={}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())

pprint(get('http://localhost:5000/api/news').json())
