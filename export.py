import numpy as np
import pandas as pd
import mysql.connector
from mysql.connector import Error


def SaveIntoFile():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='safety',
                                             user='root',
                                             password='')

        sql_select_Query = "select * from accident_list"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        columns = [desc[0] for desc in cursor.description]
        records = cursor.fetchall()
        for row in records:
            df = pd.DataFrame(list(records), columns=columns)
        print(df)

        df.to_excel('try.xlsx')
        #without index in excel file
        df.to_excel('try.xlsx', index = False)
            
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


