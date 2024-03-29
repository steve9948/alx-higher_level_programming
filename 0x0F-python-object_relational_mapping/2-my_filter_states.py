#!/usr/bin/python3
"""states models
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306
    state_name = sys.argv[4]  # "your_database_name"
    query = "SELECT * FROM states WHERE name LIKE BINARY\
 '{}' ORDER BY id ASC".format(state_name)
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    # launch the cursor
    cursor = db.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    """Print the rows"""
    for row in rows:
        print(row)

    """Close the cursor"""
    cursor.close()
    db.close()
