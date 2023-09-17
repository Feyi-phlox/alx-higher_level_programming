#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a'
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all State objects containing the letter 'a' sorted by id
    obj = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()

    for state in obj:
        print("{}: {}".format(state.id, state.name))

    session.close()
