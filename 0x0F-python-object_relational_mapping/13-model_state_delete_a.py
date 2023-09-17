#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the 'a'
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

    # Query and delete all State objects with a name containing 'a'
    states_to_del = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_del:
        session.delete(state)

    session.commit()
    session.close()
