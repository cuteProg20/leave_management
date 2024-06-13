from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from extensions import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))
    country_id = Column(Integer, ForeignKey('countries.id'))
    name = Column(String(128), nullable=False)
    position = Column(String(64))

    user = relationship('User', back_populates='employee')
    department = relationship('Department', back_populates='employees')
    country = relationship('Country', back_populates='employees')
    leave_requests = relationship('LeaveRequest', back_populates='employee')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'department_id': self.department_id,
            'country_id': self.country_id,
            'name': self.name,
            'position': self.position,
            'user': self.user.to_dict() if self.user else None,
            'department': self.department.to_dict() if self.department else None,
            'country': self.country.to_dict() if self.country else None
        }
