from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from flask_login import login_user, logout_user, current_user, login_required
from ..models import User
from extensions import db

auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

class RegisterAPI(Resource):
    def post(self):
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'User already exists'}), 400

        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201

class LoginAPI(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            login_user(user)
            token = user.generate_token()
            return jsonify({'token': token, 'user': user.to_dict()})
        return jsonify({'message': 'Invalid username or password'}), 401

class LogoutAPI(Resource):
    @login_required
    def post(self):
        logout_user()
        return '', 204

class ProtectedAPI(Resource):
    @login_required
    def get(self):
        return jsonify({'message': f'Hello, {current_user.username}!'})

class TokenVerifyAPI(Resource):
    def post(self):
        token = request.get_json().get('token')
        user = User.verify_token(token)
        if user:
            return jsonify({'user': user.to_dict()})
        return jsonify({'message': 'Invalid or expired token'}), 401

api.add_resource(RegisterAPI, '/register')
api.add_resource(LoginAPI, '/login')
api.add_resource(LogoutAPI, '/logout')
api.add_resource(ProtectedAPI, '/protected')
api.add_resource(TokenVerifyAPI, '/token-verify')
