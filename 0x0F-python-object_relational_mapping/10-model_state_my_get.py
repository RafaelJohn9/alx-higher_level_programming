#!/usr/bin/python3

"""
a script that prints the state object with the name passed as arg
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    """
    a script that prints the state obj
    with the name passed as arg from the database
    """

    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    # extraction of arg passed
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    stateSearched = sys.argv[4]

    # creating engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                name,
                passwd,
                dbname
                )
            )

    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query being made and printed
    """
    state must be thinned out to the object it self through .first()
    this is because if you don't it is taken as a fullquery even if it is one
    element thus it is impossible to check if state is null or not
    or
    you can loop through the one element and check if state of states is null
    or
    not
    """
    state = session.query(State).filter(State.name == stateSearched).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
