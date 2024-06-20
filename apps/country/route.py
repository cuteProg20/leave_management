from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from ..models import Country
from ...extensions import db

country_bp = Blueprint('country', __name__)
api = Api(country_bp)

class CountryListAPI(Resource):
    def get(self):
        countries = Country.query.all()
        return jsonify([country.to_dict() for country in countries])

    def post(self):
        data = request.get_json()
        country = Country(name=data['name'], code=data['code'])
        db.session.add(country)
        db.session.commit()
        return jsonify(country.to_dict()), 201

class CountryAPI(Resource):
    def get(self, country_id):
        country = Country.query.get_or_404(country_id)
        return jsonify(country.to_dict())

    def put(self, country_id):
        country = Country.query.get_or_404(country_id)
        data = request.get_json()
        country.name = data.get('name', country.name)
        country.code = data.get('code', country.code)
        db.session.commit()
        return jsonify(country.to_dict())

    def delete(self, country_id):
        country = Country.query.get_or_404(country_id)
        db.session.delete(country)
        db.session.commit()
        return '', 204

api.add_resource(CountryListAPI, '/')
api.add_resource(CountryAPI, '/<int:country_id>')
