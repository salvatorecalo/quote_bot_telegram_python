import sqlite3

def create_user_table():
    conn = sqlite3.connect('db/users.db')
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users (
                       user_id TEXT PRIMARY KEY
                       )
                """)
    conn.commit()
    conn.close()