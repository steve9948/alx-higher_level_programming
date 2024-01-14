#!/usr/bin/python3
"""
Module States
script that lists all cities from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db_host = "localhost"
    db_user = sys.argv[1]  # "username"
    db_password = sys.argv[2]  # "password"
    db_name = sys.argv[3]  # "database_name"
    port = 3306
    state_name = sys.argv[4]  # "your_database_name"
    query = "SELECT name FROM cities WHERE state_id = \
(SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id ASC"
    params = (state_name,)

    # Launch the db connection
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )

    # Launch the cursor connection
    cursor = db.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()
    tuples = ()

    # Print the rows
    for row in rows:
        tuples += row
    print(*tuples, sep=", ")

    # Terminate the cursor
    cursor.close()

    # Close the db
    db.close()
