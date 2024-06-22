from flask import Blueprint
from flask_restful import Api

from ..models import User
from .route import RegisterAPI, LoginAPI, LogoutAPI, ProtectedAPI, TokenVerifyAPI

# Create a Blueprint for authentication
auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

# Add routes to the API
api.add_resource(RegisterAPI, '/register')
api.add_resource(LoginAPI, '/login')
api.add_resource(LogoutAPI, '/logout')
api.add_resource(ProtectedAPI, '/protected')
api.add_resource(TokenVerifyAPI, '/token-verify')

# User loader function for Flask-Login
from extensions import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))