#!/usr/bin/python3
"""states models
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "Username"
    db_password = sys.argv[2]  # "Password"
    db_name = sys.argv[3]  # "Name"
    port = 3306  # "Port"

    # Connect to the database
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    # Launch the cursor
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON states.id = cities.state_id \
    ORDER BY cities.id")
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Terminate the cursor
    cursor.close()

    # Terminate connection to the DB
    db.close()
