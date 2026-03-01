#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states \
             WHERE name LIKE BINARY '{}' \
             ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
