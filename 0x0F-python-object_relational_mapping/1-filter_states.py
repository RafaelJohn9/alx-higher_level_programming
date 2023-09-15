#!/usr/bin/python3

"""
a script that lists all states with a name starting with n from the database
"""

if __name__ == "__main__":
    """
    a script that lists all states
    """
    import sys
    import MySQLdb

    # the arg passed
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    # the connection
    sql = MySQLdb.connect
    db = sql(host="localhost", user=name, passwd=passwd, db=dbname, port=3036)

    # starting the cursor
    cur = db.cursor()

    # processing of query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY ID ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    # close connection
    cur.close()
    db.close()
