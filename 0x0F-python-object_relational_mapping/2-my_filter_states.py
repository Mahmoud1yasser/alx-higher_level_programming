#!/usr/bin/python3
'''takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.'''
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    query = """SELECT * FROM states 
    WHERE name LIKE '{}'ORDER BY id ASC""".format(name)
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        if state[1] == name:
            print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
