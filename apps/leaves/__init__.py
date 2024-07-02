from flask import Blueprint
from flask_restful import Api
from .route import LeaveListAPI, LeaveAPI


# Create a Blueprint for department management
leave_bp = Blueprint('leaves', __name__)
api = Api(leave_bp)

# Add resources (routes) to the API
api.add_resource(LeaveListAPI, '/')
api.add_resource(LeaveAPI, '/<int:leave_id>')