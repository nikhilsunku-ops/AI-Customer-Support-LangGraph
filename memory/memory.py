from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3


def get_checkpointer(db_path: str = "memory/memory.db"):
    """
    Creates and returns a SQLite-based LangGraph checkpointer.
    The database file is created automatically if it doesn't exist.
    """

    conn = sqlite3.connect(db_path, check_same_thread=False)
    return SqliteSaver(conn)