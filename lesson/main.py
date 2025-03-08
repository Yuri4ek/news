from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

db_session.global_init("db/blogs.db")

if False:
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'U'
    user.name = 'X'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'engineer PROF'
    user.address = 'module_1'
    user.email = 'blabla@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Antonio'
    user.name = 'Yuriy'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'processor'
    user.address = 'module_001'
    user.email = 'AY123456789@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Dima'
    user.name = 'Dima'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'engineer'
    user.address = 'module_2'
    user.email = 'DDima@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

if True:
    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = 15
    jobs.collaborators = '2, 3'
    jobs.start_date = None
    jobs.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()
