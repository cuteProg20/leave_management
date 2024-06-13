from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from extensions import db

class Department(db.Model):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    description = Column(String(255))
    employees = relationship('Employee', back_populates='department')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
