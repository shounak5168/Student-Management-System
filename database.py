import sqlite3

def connect_db():
    """Connect to the SQLite database (or create one if it doesn't exist)."""
    return sqlite3.connect("students.db")

def initialize_db():
    """Create the students table if it doesn't exist."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()
