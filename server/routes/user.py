from flask import request, make_response
from sqlalchemy.exc import IntegrityError
from flask_restful import Resource
from models.models import User
from config import api, db

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)
    
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get("password")

        try:
            user = User(username=username)
            user.password_hash = password

            db.session.add(user)
            db.session.commit()

            return user.to_dict(), 201
        except IntegrityError:
            return {'error': 'Username must be unique'}, 422
    
api.add_resource(Users, '/api/users')


class UserResource(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return user.to_dict(), 200

api.add_resource(UserResource, '/api/users/<int:id>')