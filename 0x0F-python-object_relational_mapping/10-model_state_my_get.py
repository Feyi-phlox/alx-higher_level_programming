#!/usr/bin/python3
"""
Script that prints the State object with the name passed
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statenam = sys.argv[4]

    # Create an SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter_by(name=statenam).first()

        if state:
            print("{}".format(state.id))
        else:
            print("Not found")
    except IntegrityError as e:
        print("Error:", e)

    session.close()
