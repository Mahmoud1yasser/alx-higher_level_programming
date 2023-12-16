#!/usr/bin/python3
'''takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.'''
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE %s\
            ORDER by cities.id ASC"""
    cur.execute(query, (state_name,))
    cities = cur.fetchall()
    for city in cities:
        print("{}, ".format(city[1]), end='')
    print("\n")
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
