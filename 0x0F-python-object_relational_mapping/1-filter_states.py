#!/usr/bin/python3
"""
Model States
script lists  N
from  hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    MY_USER = argv[1]
    MY_PASSWD = argv[2]
    MY_DB = argv[3]

    '''Open Database connection'''
    mydb = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=MY_USER,
                           passwd=MY_PASSWD,
                           db=MY_DB)

    '''Create cursor to the DB'''
    myCursor = mydb.cursor()

    '''pass and execute SQL'''
    myCursor.execute("select * from states \
                     where name like 'N%'\
                     order by id asc")

    '''Get the records and fill cursor'''
    states = myCursor.fetchall()

    '''Print rows'''
    for state in states:
        print(state)

    '''close the cursor'''
    myCursor.close()

    '''Terminate connection to DB'''
    mydb.close()
