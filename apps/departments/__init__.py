from flask import Blueprint
from flask_restful import Api
from .route import DepartmentListAPI, DepartmentAPI, DepartmentsByCountryAPI

# Create a Blueprint for department management
department_bp = Blueprint('department', __name__)
api = Api(department_bp)

# Add resources (routes) to the API
api.add_resource(DepartmentListAPI, '/')
api.add_resource(DepartmentAPI, '/<int:department_id>')
api.add_resource(DepartmentsByCountryAPI, '/country/<int:country_id>')