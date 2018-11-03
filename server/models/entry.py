from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models import db, person

class Entry(db.Model):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    personId = Column(Integer, ForeignKey('people.id'))
    date = Column(Date, nullable=False)
    type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    location = Column(String, nullable=True)
    description = Column(String, nullable=False)

    person = relationship("Person", back_populates="entries")

    def __init__(self, date, title, description, type, location):
        # self.personId = personId
        self.date = date
        self.title = title
        self.description = description
        self.type = type
        self.location = location


    def __repr__(self):
        return "<Entry(id='" + self.id + "', title='" + self.title + "')>"

person.entries = relationship("Entry", order_by=Entry.id, back_populates="Person")

