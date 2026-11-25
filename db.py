import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "scanner_results.db")


def get_db():
    return sqlite3.connect(DB_NAME, check_same_thread=False, timeout=10)


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS open_ports (
            port INTEGER,
            activity TEXT,
            risk INTEGER,
            source_ip TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS honeypot_logs (
            ip TEXT,
            port INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()