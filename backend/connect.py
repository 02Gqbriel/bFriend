import sqlite3
import json


def connect_database(prep_stmt, *args):
    sql_conn = sqlite3.connect('../database/sqlite.db')
    sql_conn.row_factory = sqlite3.Row
    cursor = sql_conn.cursor()

    if args:
        try:
            cursor.execute(prep_stmt, args)
            sql_conn.commit()
            rows = cursor.fetchall()

            response = [dict(row) for row in rows]

            json_response = json.dumps(response)
            return json_response
        except sqlite3.Error as error:
            sql_conn.rollback()
            return json.dumps(str(error))
    else:
        try:
            cursor.execute(prep_stmt)
            sql_conn.commit()
            rows = cursor.fetchall()
            sql_conn.close()

            response = [dict(row) for row in rows]

            json_response = json.dumps(response)
            return json_response
        except sqlite3.Error as error:
            sql_conn.rollback()
            return json.dumps(str(error))
