import sqlite3
from .setup_logger import setup_logger
logger =setup_logger(__name__)

def save_user_to_db(user_id: str) -> None:
    logger.info(f"Saving user {user_id} to database")
    conn = sqlite3.connect("db/users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()
    