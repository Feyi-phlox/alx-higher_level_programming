#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statenam = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    cur = db.cursor()
    query = """SELECT cities.name FROM cities \
            INNER JOIN states ON states.id = cities.state_id \
            WHERE states.name = %s ORDER BY cities.id ASC"""

    cur.execute(query, (statenam,))

    results = cur.fetchall()

    citynames = [row[0] for row in results]
    print(", ".join(citynames))

    cur.close()
    db.close()
