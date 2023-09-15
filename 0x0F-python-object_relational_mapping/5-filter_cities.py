#!/usr/bin/python3

"""
a script that lists all cities from the database hbtn_0e_4)usa"
"""

if __name__ == "__main__":
    """
    a python script that creates a query
    """

    import sys
    import MySQLdb

    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    query = sys.argv[4]

    # connect the sql db
    sql = MySQLdb.connect
    db = sql(host='localhost', user=name, passwd=passwd, db=dbname)

    # start the sql query
    cur =  db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name=%s ORDER BY cities.id ASC", (query, ))
    cities = cur.fetchall()

    listOfStates = []
    for state in cities:
        for city in state:
            listOfStates.append(city)

    print(', '.join(listOfStates))

    db.close()
    cur.close()
