from flask import request, jsonify
from flask_restful import Resource
from ..models import Department, Country
from ...extensions import db

class DepartmentListAPI(Resource):
    def get(self):
        departments = Department.query.all()
        return jsonify([department.to_dict() for department in departments])

    def post(self):
        data = request.get_json()
        country_id = data.get('country_id')
        country = Country.query.get(country_id)
        
        if not country:
            return jsonify({'message': 'Country not found'}), 404

        department = Department(name=data['name'], country=country)
        db.session.add(department)
        db.session.commit()
        return jsonify(department.to_dict()), 201

class DepartmentAPI(Resource):
    def get(self, department_id):
        department = Department.query.get_or_404(department_id)
        return jsonify(department.to_dict())

    def put(self, department_id):
        department = Department.query.get_or_404(department_id)
        data = request.get_json()
        country_id = data.get('country_id')

        if country_id:
            country = Country.query.get(country_id)
            if not country:
                return jsonify({'message': 'Country not found'}), 404
            department.country = country

        department.name = data.get('name', department.name)
        db.session.commit()
        return jsonify(department.to_dict())

    def delete(self, department_id):
        department = Department.query.get_or_404(department_id)
        db.session.delete(department)
        db.session.commit()
        return '', 204

class DepartmentsByCountryAPI(Resource):
    def get(self, country_id):
        country = Country.query.get_or_404(country_id)
        departments = Department.query.filter_by(country_id=country.id).all()
        return jsonify([department.to_dict() for department in departments])

