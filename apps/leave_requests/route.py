from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from ..models import LeaveRequest, LeaveStatus
from ...extensions import db

leave_request_bp = Blueprint('leave_request', __name__)
api = Api(leave_request_bp)

class LeaveRequestListAPI(Resource):
    def get(self):
        leave_requests = LeaveRequest.query.all()
        return jsonify([leave_request.to_dict() for leave_request in leave_requests])

    def post(self):
        data = request.get_json()
        leave_request = LeaveRequest(
            employee_id=data['employee_id'],
            leave_type_id=data['leave_type_id'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            reason=data.get('reason'),
            status=LeaveStatus[data.get('status', 'PENDING')]
        )
        if 'country_id' in data:
            leave_request.country_id = data['country_id']
        db.session.add(leave_request)
        db.session.commit()
        return jsonify(leave_request.to_dict()), 201

class LeaveRequestAPI(Resource):
    def get(self, leave_request_id):
        leave_request = LeaveRequest.query.get_or_404(leave_request_id)
        return jsonify(leave_request.to_dict())

    def put(self, leave_request_id):
        leave_request = LeaveRequest.query.get_or_404(leave_request_id)
        data = request.get_json()
        leave_request.start_date = data.get('start_date', leave_request.start_date)
        leave_request.end_date = data.get('end_date', leave_request.end_date)
        leave_request.reason = data.get('reason', leave_request.reason)
        leave_request.status = LeaveStatus[data.get('status', leave_request.status.name)]
        if 'country_id' in data:
            leave_request.country_id = data['country_id']
        db.session.commit()
        return jsonify(leave_request.to_dict())

    def delete(self, leave_request_id):
        leave_request = LeaveRequest.query.get_or_404(leave_request_id)
        db.session.delete(leave_request)
        db.session.commit()
        return '', 204

api.add_resource(LeaveRequestListAPI, '/')
api.add_resource(LeaveRequestAPI, '/<int:leave_request_id>')
