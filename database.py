import sqlite3

def get_db_connection():
    conn = sqlite3.connect("weather.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            timestamp TEXT PRIMARY KEY,
            temperature REAL,
            humidity REAL
        )
    """)
    conn.commit()
    conn.close()