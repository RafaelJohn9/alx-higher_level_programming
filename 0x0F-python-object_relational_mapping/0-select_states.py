#!/usr/bin/python3

"""
a script that lists all states  from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    """ a script that executes sql query in relation to python code """
    import sys
    import MySQLdb

    # arg being passed
    argPassed = sys.argv
    name = argPassed[1]
    passwd = argPassed[2]
    dbname = argPassed[3]

    # db being connected to
    sql = MySQLdb.connect
    db = sql(host="localhost", user=name, passwd=passwd, db=dbname, port=3306)

    cur = db.cursor()
    # query is written, stored and printed out
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    # close connection
    cur.close()
    db.close()
