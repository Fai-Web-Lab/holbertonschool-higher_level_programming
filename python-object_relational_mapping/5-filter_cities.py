#!/usr/bin/python3
"""
Lists all cities of a specific state from the database hbtn_0e_4_usa.
The state name is passed as an argument and protected from SQL injection.
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

    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))

    query_rows = cursor.fetchall()

    print(", ".join(city[0] for city in query_rows))

    cursor.close()
    db.close()
