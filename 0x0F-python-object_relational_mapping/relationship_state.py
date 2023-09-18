#!/usr/bin/python3
"""
This module defines the State class for relationship_state.
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_city import Base


class State(Base):
    """
    State class represents the 'states' table in the database.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all,\
                            delete-orphan")
