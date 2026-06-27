import sqlite3

DB_NAME = "memory.db"


def initialize_database():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_name TEXT,

        query TEXT,

        response TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_conversation(customer_name, query, response):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations
        (customer_name, query, response)
        VALUES (?, ?, ?)
        """,
        (customer_name, query, response)
    )

    conn.commit()
    conn.close()


def get_last_query(customer_name):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT query
        FROM conversations
        WHERE customer_name = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (customer_name,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None