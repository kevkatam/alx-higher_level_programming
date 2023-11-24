#!/usr/bin/python3
"""
module containing a class definition of City and that inherits from base
"""
from model_state import Base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ class that defines city """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
