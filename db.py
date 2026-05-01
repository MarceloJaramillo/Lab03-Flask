import sqlite3

DATABASE = "lab03_flask.db"

def get_connection():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion