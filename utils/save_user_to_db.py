import sqlite3

def save_user_to_db(user_id: str) -> None:
    conn = sqlite3.connect("db/users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()
    