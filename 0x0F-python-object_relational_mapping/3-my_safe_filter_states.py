#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. Safe from injenctions
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)

    cur = db.cursor()
    query = ("SELECT * FROM states\
              WHERE name = %s\
              ORDER BY states.id;")
    cur.execute(query, (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
