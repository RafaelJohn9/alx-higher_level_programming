#!/usr/bin/python3

"""
improve the files model_city.py
and model_state.py
"""

if __name__ == "__main__":
    """
    improved the files model city
    and model state
    """

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.engine.url import URL

    if __name__ == "__main__":
        """
        a script that creates a state and a city
        """
        db = {
                'drivername': 'mysql+mysqldb',
                'host': 'localhost',
                'port': '3306',
                'username': sys.argv[1],
                'password': sys.argv[2],
                'database': sys.argv[3]}

        url = URL.create(**db)
        engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        new_city = City(name="San Francisco")
        new_state = State(name="California", cities=[new_city])

        session.add(new_city)
        session.add(new_state)
        session.commit()

        session.close()
