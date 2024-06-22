from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from extensions import db

class Leaves(db.Model):
    __tablename__ = 'leaves'

    id = Column(Integer, primary_key=True)


class LeaveType(db.Model):
    __tablename__ = 'leave_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    # Relationship with LeaveRequest
    leave_requests = relationship('LeaveRequest', back_populates='leave_type')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


class LeaveType(db.Model):
    __tablename__ = 'leave_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    # Relationship with LeaveRequest
    leave_requests = relationship('LeaveRequest', back_populates='leave_type')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
