from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.users import User

app = Flask(__name__)
api = Api(app)


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify({'users': users.to_dict(
            only=(
                'name', 'about', 'email', 'hashed_password', 'created_date'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'about', 'email', 'hashed_password', 'created_date'))
            for item in users]})

    def post(self):
        print('f;oaejgrwoagjiqegeklsgj;ljkag;qaengk;aeng;andgkald/gnea;lgnmd '
              'gadgnlneal/gnkeagkendgldngllllllnwlsrk.djgbsrdktguj,ser')
        args = parser.parse_args()
        print(args)
        session = db_session.create_session()
        users = User(
            name=args['name'],
            about=args['about'],
            email=args['email'],
            hashed_password=args['hashed_password'],
            created_date=args['created_date']
        )
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"Users {users_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('about', required=True)
parser.add_argument('email', required=True, type=bool)
parser.add_argument('hashed_password', required=True, type=bool)
parser.add_argument('created_date', required=True, type=int)
