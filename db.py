import os

import turso

DATABASE_URL = os.getenv("DATABASE_URL", "numbers.db")
DATABASE_AUTH_TOKEN = os.getenv("DATABASE_AUTH_TOKEN")


def get_connection():
    if DATABASE_AUTH_TOKEN:
        return turso.connect(DATABASE_URL, auth_token=DATABASE_AUTH_TOKEN)
    return turso.connect(DATABASE_URL)


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seven_digit INTEGER NOT NULL,
            long_digit TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def store_numbers(seven_digit: int, long_digit: str):
    conn = get_connection()
    conn.execute(
        "INSERT INTO numbers (seven_digit, long_digit) VALUES (?, ?)",
        (seven_digit, long_digit),
    )
    conn.commit()
    conn.close()


def get_all_numbers():
    conn = get_connection()
    cursor = conn.execute(
        "SELECT id, seven_digit, long_digit, created_at FROM numbers ORDER BY created_at DESC"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
