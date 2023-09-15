#!/usr/bin/python3

"""
a script that prints all city objects
from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    """
    a script that prints all city obj
    """

    import sys
    from sqlalchemy import create_engine
    from model_city import City
    from model_state import State
    from sqlalchemy.orm import sessionmaker

    # extraction of arg
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    # create engine
    engine = create_engine(
            f"mysql+mysqldb://{name}:{passwd}@localhost:3306/{dbname}"
            )

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # a query
    query = (
            session.query(City, State)
            .join(State, City.state_id == State.id)
            .order_by(City.id)
            )

    # print all cities
    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    # close the session
    session.close()
