from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from ..models import Employee
from ...extensions import db

employee_bp = Blueprint('employee', __name__)
api = Api(employee_bp)

class EmployeeListAPI(Resource):
    def get(self):
        employees = Employee.query.all()
        return jsonify([employee.to_dict() for employee in employees])

    def post(self):
        data = request.get_json()
        employee = Employee(
            user_id=data['user_id'],
            department_id=data.get('department_id'),
            country_id=data.get('country_id'),
            name=data['name'],
            position=data.get('position')
        )
        db.session.add(employee)
        db.session.commit()
        return jsonify(employee.to_dict()), 201

class EmployeeAPI(Resource):
    def get(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        return jsonify(employee.to_dict())

    def put(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        data = request.get_json()
        employee.name = data.get('name', employee.name)
        employee.position = data.get('position', employee.position)
        employee.department_id = data.get('department_id', employee.department_id)
        employee.country_id = data.get('country_id', employee.country_id)
        db.session.commit()
        return jsonify(employee.to_dict())

    def delete(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return '', 204

api.add_resource(EmployeeListAPI, '/')
api.add_resource(EmployeeAPI, '/<int:employee_id>')
