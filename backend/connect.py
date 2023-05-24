import sqlite3
import json


def connect_database(prep_stmt, *args):
    sql_conn = sqlite3.connect('../database/sqlite.db')
    cursor = sql_conn.cursor()

    if args:
        try:
            cursor.execute(prep_stmt, args)
            sql_conn.commit()
            response = cursor.fetchall()
            sql_conn.close()
            if len(response) == 1:
                return json.dumps(response[0])
            else:
                return json.dumps(response)
        except sqlite3.Error as error:
            sql_conn.rollback()
            return str(error)
    else:
        try:
            cursor.execute(prep_stmt)
            sql_conn.commit()
            response = cursor.fetchall()
            result = [
                dict(zip(["ID", "Username", "Password", "First Name", "Last Name", "Age", "Hobby", "Status"], row)) for
                row in response]
            json_data = json.dumps(result)
            sql_conn.close()
            if len(response) == 1:
                return json.dumps(response[0])
            else:
                return json_data
        except sqlite3.Error as error:
            sql_conn.rollback()
            return str(error)