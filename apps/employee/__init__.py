from flask import Blueprint
from flask_restful import Api
from .route import EmployeeListAPI, EmployeeAPI

# Create a Blueprint for department management
employee_bp = Blueprint('department', __name__)
api = Api(employee_bp)

# Add resources (routes) to the API
api.add_resource(EmployeeListAPI, '/')
api.add_resource(EmployeeAPI, '/<int:department_id>')