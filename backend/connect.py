import sqlite3


def connect_database(prep_stmt, *args):
    sql_conn = sqlite3.connect('../database/sqlite.db')
    cursor = sql_conn.cursor()
    # only prep_stmt required e.g: connect_database("SELECT * ...", None)
    if args is None:
        try:
            cursor.execute(prep_stmt)
            sql_conn.commit()  # Commit the transaction
            sql_conn.close()
            return "created"
        except sqlite3.Error as error:
            sql_conn.rollback()
            return str(error)
    # prep_stmt AND values required e.g: connect_database("SELECT * ... WHERE column1 = ?...", value1, ...)
    else:
        try:
            cursor.execute(prep_stmt, args)
            sql_conn.commit()  # Commit the transaction
            response = cursor.fetchall()
            sql_conn.close()
            return response
        except sqlite3.Error as error:
            sql_conn.rollback()
            return str(error)
