from functools import wraps
from flask import request, jsonify
from ..models import User

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            token = token.split(" ")[1]  # Remove Bearer prefix
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        user = User.verify_token(token)
        if not user:
            return jsonify({'message': 'Invalid or expired token'}), 401

        return f(user, *args, **kwargs)
    return decorated_function