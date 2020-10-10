# modules for sending notification
import mysql.connector
import datetime

HOST = "localhost"
USER = "root"
PASSWORD = "admin"
DATABASE = "safety"

# accepts unique id, location string
# updates the local database with time and location of accident.
def insert(aId, aLocation):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='safety',
                                             user='root',
                                             password='')

        mycursor = connection.cursor()
        lDatetime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        print(lDatetime)
        sql = "INSERT INTO accident_list (BotID, location, date_time) VALUES ({}, '{}', '{}')".format(aId, aLocation, lDatetime)

        mycursor.execute(sql)
        connection.commit()

    finally:
        if (connection.is_connected()):
            connection.close()
            mycursor.close()
            print("MySQL connection is closed")

