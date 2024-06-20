from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash
from ..models import User
from ...extensions import db

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

class UserListAPI(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    def post(self):
        data = request.get_json()
        password_hash = generate_password_hash(data['password'])
        user = User(username=data['username'], email=data['email'], password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201

class UserAPI(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        if 'password' in data:
            user.password_hash = generate_password_hash(data['password'])
        db.session.commit()
        return jsonify(user.to_dict())

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

api.add_resource(UserListAPI, '/')
api.add_resource(UserAPI, '/<int:user_id>')
