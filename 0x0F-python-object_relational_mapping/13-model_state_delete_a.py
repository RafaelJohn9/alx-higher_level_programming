#!/usr/bin/python3

"""
a script that deletes all state objects with a name containing a
from the database
"""

if __name__ == "__main__":
    """
    a script that deletes all state objects
    """

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    # extraction of arg
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    # create engine
    engine = create_engine(
            f"mysql+mysqldb://{name}:{passwd}@localhost:3306/{dbname}"
            )

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create  query
    # states to be deleted
    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)
    session.commit()

    for element in dir(session):
        if element[0] == '_':
            continue
        else:
            print(element)

    session.close()
