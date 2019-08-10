#!/usr/bin/python3
"""Module to list states in a database"""


import MySQLdb
import sys


def main():
    """List the names and IDs of U.S. states in a database"""

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM `states` ORDER BY `id` ASC;')
    records = cursor.fetchall()
    print('\n'.join(str(record) for record in records))
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
