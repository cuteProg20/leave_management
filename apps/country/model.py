from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from extensions import db

class Country(db.Model):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    code = Column(String(3), unique=True, nullable=False)  # ISO country code
    employees = relationship('Employee', back_populates='country')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code
        }