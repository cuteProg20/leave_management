from flask import Blueprint
from flask_restful import Api
from .route import CountryListAPI, CountryAPI

# Create a Blueprint for country management
country_bp = Blueprint('country', __name__)
api = Api(country_bp)

# Add resources (routes) to the API
api.add_resource(CountryListAPI, '/')
api.add_resource(CountryAPI, '/<int:country_id>')