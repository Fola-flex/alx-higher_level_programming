#!/usr/bin/python3
""" list all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], 
                        password=sys.argv[2], database=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.state_id""")
    row = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
