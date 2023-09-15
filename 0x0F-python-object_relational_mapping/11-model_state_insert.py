#!/usr/bin/python3

"""
a script that adds the State obj 'Louisiana' to the database
hbtn_0e_6_usa
"""

if __name__ == "__main__":
    """
    a script that adds the state object "Louisiana" to the database
    """

    # libraries import
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    # extraction of arg
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    # creation of engine
    engine = create_engine(f"mysql+mysqldb://{name}:{passwd}//@localhost:3036/{dbname}")

    # session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create query
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # print the new state id
    print(new_state.id)

    session.close()
