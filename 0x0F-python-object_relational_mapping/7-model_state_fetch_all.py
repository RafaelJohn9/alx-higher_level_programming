#!/usr/bin/python3

"""
a script that lists all state objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    # library & functions being imported
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # extract arguments
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    # create and sqlalchemy engine to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(name, passwd, dbname))

    # create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all State objects in ascending order
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    # close the session
    session.close()
