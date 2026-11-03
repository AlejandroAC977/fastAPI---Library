import sqlite3
#from pathlib import Path

class SqlBookRepository:
    def __init__(self, db_path: str = "library.db"):
        self.db_path = db_path
        self._initializace_database()

    def _initializace_database(self):
        with sqlite3.connect(self.db_path) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL
                )
            """)

    def get_all(self) -> list[dict]:
        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row

            rows = connection.execute(
                "SELECT id, title, author from books"
            ).fetchall()

            return [dict(row) for row in rows]

    def get_by_id(self, book_id) -> dict | None:
        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row

            row = connection.execute(
                "SELECT id, title, author from books WHERE id = ?", (book_id,)
            ).fetchone()

            return dict(row) if row else None

    def create(self, title: str, author: str) -> list[dict]:
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(
                "INSERT INTO books (title, author) VALUES (?, ?)", (title, author)
            )

            book_id = cursor.lastrowid

            return {
                "id": book_id,
                "title": title,
                "author": author
            }
