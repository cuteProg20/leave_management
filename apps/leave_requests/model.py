from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, DateTime
from sqlalchemy.orm import relationship
from extensions import db
import enum

class LeaveStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class LeaveRequest(db.Model):
    __tablename__ = 'leave_requests'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    leave_type_id = Column(Integer, ForeignKey('leave_types.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    reason = Column(String(255))
    status = Column(Enum(LeaveStatus), default=LeaveStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    employee = relationship('Employee', back_populates='leave_requests')
    leave_type = relationship('LeaveType', back_populates='leave_requests')

    def to_dict(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'leave_type_id': self.leave_type_id,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'reason': self.reason,
            'status': self.status.value,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'employee': {
                'id': self.employee.id,
                'name': self.employee.name
            },
            'leave_type': {
                'id': self.leave_type.id,
                'name': self.leave_type.name
            }
        }
