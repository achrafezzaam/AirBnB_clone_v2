#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ''

        @propety
        def cities(self):
            from models import storage
            linked_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id = self.id:
                    linked_cities.appen(city)
            return linked_cities
