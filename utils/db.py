import sqlite3
from flask import g
DB_PATH = "artistick.db"

def get_connection():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        g._database = conn
    return conn

def close_connection(app):
    @app.teardown_appcontext
    def close_conn(exception):
        conn = getattr(g, '_database', None)
        if conn is not None:
            conn.close()
