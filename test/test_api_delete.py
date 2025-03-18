from requests import get, delete
from pprint import pprint

print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/news/2').json())

pprint(get('http://localhost:5000/api/news').json())
