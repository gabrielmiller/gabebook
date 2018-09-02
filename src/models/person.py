from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship
from models import db

class Person(db.Model):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    metOn = Column(Date, nullable=True)
    metPlace = Column(String, nullable=True)
    knowFrom = Column(String, nullable=True)
    livesIn = Column(String, nullable=True)
    originallyFrom = Column(String, nullable=True)
    college = Column(String, nullable=True)
    collegeStudied = Column(String, nullable=True)
    jobTitle = Column(String, nullable=True)
    jobDescription = Column(String, nullable=True)

    def __init__(self, firstName, lastName, metOn):
        self.firstName = firstName
        self.lastName = lastName
        self.metOn = metOn

    def __repr__(self):
        return "<Person(firstName='" + self.firstName + "', lastName='" + self.lastName + "')>"

