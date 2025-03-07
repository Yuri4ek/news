from data import db_session
from data.users import User

db_session.global_init("db/blogs.db")

'''user = User()
user.name = "Пользователь 3"
user.about = "биография пользователя 3"
user.email = "email3@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()'''

db_sess = db_session.create_session()
users = db_sess.query(User).all()

for user in users:
    print(user)