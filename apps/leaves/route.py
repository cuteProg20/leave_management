from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from .model import LeaveRequest
from .. import db

leave_bp = Blueprint('leave', __name__)
api = Api(leave_bp)

class LeaveListAPI(Resource):
    def get(self):
        leaves = LeaveRequest.query.all()
        return jsonify([leave.to_dict() for leave in leaves])

    def post(self):
        data = request.get_json()
        leave = LeaveRequest(**data)
        db.session.add(leave)
        db.session.commit()
        return jsonify(leave.to_dict()), 201

class LeaveAPI(Resource):
    def get(self, leave_id):
        leave = LeaveRequest.query.get_or_404(leave_id)
        return jsonify(leave.to_dict())

    def put(self, leave_id):
        leave = LeaveRequest.query.get_or_404(leave_id)
        data = request.get_json()
        for key, value in data.items():
            setattr(leave, key, value)
        db.session.commit()
        return jsonify(leave.to_dict())

    def delete(self, leave_id):
        leave = LeaveRequest.query.get_or_404(leave_id)
        db.session.delete(leave)
        db.session.commit()
        return '', 204

api.add_resource(LeaveListAPI, '/')
api.add_resource(LeaveAPI, '/<int:leave_id>')
