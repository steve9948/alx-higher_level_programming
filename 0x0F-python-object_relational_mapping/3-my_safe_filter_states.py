#!/usr/bin/python3
"""
Module States
lists all states from db hbtn_0e_0_usa
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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    params = (state_name,)
    
    # Launch the db
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    # Launch the cursor
    cursor = db.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    # Print the rows
    for row in rows:
        print(row)
    
    # Terminate the cursor
    cursor.close()
    db.close()
