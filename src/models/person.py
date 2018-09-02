from sqlalchemy import Column, Date, Integer, String
from models import db

class Person(db.Model):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    metOn = Column(Date, nullable=True)

    def __init__(self, firstName, lastName, metOn):
        self.firstName = firstName
        self.lastName = lastName
        self.metOn = metOn

    def __repr__(self):
        return "<Person(firstName='" + self.firstName + "', lastName='" + self.lastName + "')>"

