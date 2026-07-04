import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "demo.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            email TEXT,
            is_admin INTEGER DEFAULT 0
        )
        """
    )
    conn.execute(
        "INSERT OR IGNORE INTO users (username, password, email, is_admin) VALUES (?, ?, ?, ?)",
        ("admin", "password123", "admin@example.com", 1),
    )
    conn.execute(
        "INSERT OR IGNORE INTO users (username, password, email, is_admin) VALUES (?, ?, ?, ?)",
        ("alice", "letmein", "alice@example.com", 0),
    )
    conn.commit()
    conn.close()
