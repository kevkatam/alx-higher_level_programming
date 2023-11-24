#!/usr/bin/python3
"""
module containing class State that inherits from class base an instance of
declarative base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class State(Base):
    """ class state with id and name of the state """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
