#!/usr/bin/python3

"""
writing a sql injection script
"""

if __name__ == '__main__':
    """
    a sql injection script
    """
    import sys
    import MySQLdb

    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    query = sys.argv[4]

    def SqlQueryValidator(query):
        return (str(query))

    query = SqlQueryValidator(query)

    # the connection
    sql = MySQLdb.connect
    db = sql(host="localhost", user=name, passwd=passwd, db=dbname, port=3306)

    # making the query
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE  states.name='{query}'")
    states = cur.fetchall()
    for state in states:
        print(state)

    # close all
    cur.close()
    db.close()
