from flask import Blueprint
from flask_restful import Api
from .route import LeaveRequestListAPI, LeaveRequestAPI

# Create a Blueprint for department management
leave_request_bd = Blueprint('department', __name__)
api = Api(leave_request_bd)

# Add resources (routes) to the API
api.add_resource(LeaveRequestAPI, '/')
api.add_resource(LeaveRequestAPI, '/<int:leave_request_id>')