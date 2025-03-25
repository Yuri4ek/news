from requests import get, post, delete
from pprint import pprint

print(delete('http://localhost:5000//api/v2/users/999').json())
# user-a с id = 999 нет в базе

print(delete('http://localhost:5000/api/v2/users/2').json())

print(post('http://localhost:5000/api/v2/users', json={}).json())

print(post('http://localhost:5000/api/v2/users',
           json={'name': 'Gena'}).json())

print(post('http://localhost:5000/api/v2/users',
           json={'name': 'Gena', 'about': 'Cool man', 'email': '1@111',
                 'hashed_password': '1q'}).json())

pprint(get('http://localhost:5000/api/v2/users').json())
pprint(get('http://localhost:5000/api/v2/users/1').json())
