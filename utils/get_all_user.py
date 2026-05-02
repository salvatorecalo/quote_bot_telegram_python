import sqlite3

def get_all_users():
    conn = sqlite3.connect('db/users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return users