#!/usr/bin/python3

"""
a python file similar to model_state.py
named model_city.py that contains the class definition of a city
"""

from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey

class City(Base):
    """
    this is a class that creates the table city
    """
    
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
