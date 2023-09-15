#!/usr/bin/python3

"""
a script that changes the name of a State
object from the databasse hbtn_0e_6_usa
"""



if __name__ == "__main__":
    """
    a script that changes the name of a State object
    """

    # importing needed libraries
    import sys
    from sqlalchemy import create_engine
    from model_state import State
    from sqlalchemy.orm import sessionmaker

    # extract arg
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    # creating engine
    engine = create_engine(f"mysql+mysqldb://{name}:{passwd}:@localhost:3306/{dbname}")

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create query
    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
