import mysql.connector
from mysql.connector import Error


def ShowDatabase():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='safety',
                                             user='root',
                                             password='')
        print(connection)

        sql_select_Query = "select * from accident_list"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of rows in Accident_list is: ", cursor.rowcount)

        print("\nPrinting each Accident_list record")
        for row in records:
            print("accidentID = ", row[0])
            print("BotID = ", row[1])
            print("location = ", row[2])
            print("date_time = ", row[3], "\n")

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


if __name__ == '__main__':
    ShowDatabase()
