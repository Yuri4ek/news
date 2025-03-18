from requests import get
from pprint import pprint

print(get('http://localhost:5000/api/news').json())

print(get('http://localhost:5000/api/news/1').json())

print(get('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

pprint(get('http://localhost:5000/api/news/q').json())
