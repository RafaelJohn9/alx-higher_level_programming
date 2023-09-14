#!/usr/bin/python3

"""
a script that takes in an arg and displays all values
in the states table of hbtn_0e_0_usa where name matches the arg
"""

if __name__=="__main__":
    """the python script"""
    import sys
    import MySQLdb

    # arg being passed
    name = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    query = sys.argv[4]

    #db being connected to
    sql = MySQLdb.connect
    db = sql(host="localhost", user=name, passwd=passwd, db=dbname, port=3306)

    #calling the cursor and sql query
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE states.name='{query}'")
    states =  cur.fetchall()
    for state in states:
        print(state)

    # close the connection
    cur.close()
    db.close()
