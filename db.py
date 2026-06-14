import sqlite3

LOCAL_DB_PATH = "datastar.db"


def get_connection():
    conn = sqlite3.connect(LOCAL_DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seven_digit INTEGER NOT NULL,
            long_digit INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def store_numbers(seven_digit: int, long_digit: int):
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
