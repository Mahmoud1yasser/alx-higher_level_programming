#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa")
cur = db.cursor()
query = "SELECT * FROM states ORDER BY id ASC"
cur.execute(query)
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
db.close()
