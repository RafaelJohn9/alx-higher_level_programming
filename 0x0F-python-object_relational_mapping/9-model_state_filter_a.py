#!/usr/bin/python3

"""
a script that lists all state objects that
contains the letter a from tha database
hbtn_0e_6_usa
"""

if __name__ == "__main__":
    """
    a script that lists all state objects that contains letter a
    """
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # extraction of arguments
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    # create engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(name, passwd, dbname))

    # the query part
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    states = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id).all()
            )

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
