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

    # connect the sql db
    sql = MySQLdb.connect
    db = sql(host='localhost', user=name, passwd=passwd, db=dbname)

    # start the sql query
    cur = db.cursor()
    cur.execute("SELECT * FROM cities")
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
