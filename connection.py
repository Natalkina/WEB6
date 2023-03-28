from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    conn = None
    try:
        conn = connect(host='hattie.db.elephantsql.com', user='gvyehsbp', password='X1iuWunDD1jMgcASxl_iI9E1p-nKBTzl', database='gvyehsbp', port=5432)
        yield conn
        conn.rollback()
        conn.close()
    except Error as err:
        print(err)
    finally:
        if conn:
            conn.close()
