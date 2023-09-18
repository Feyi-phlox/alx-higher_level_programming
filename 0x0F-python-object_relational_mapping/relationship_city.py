#!/usr/bin/python3
"""
Module that defines the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City class definition.

    Inherits from Base (imported from model_state).
    Links to the MySQL table cities.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
