from psycopg2 import connect, Error
from contextlib import contextmanager
from dotenv import load_dotenv
import os

load_dotenv()

@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    conn = None
    try:
        conn = connect(host=os.getenv("HOST"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), database=os.getenv("DATABASE"), port=5432)
        yield conn
        conn.rollback()
        conn.close()
    except Error as err:
        print(err)
    finally:
        if conn:
            conn.close()
