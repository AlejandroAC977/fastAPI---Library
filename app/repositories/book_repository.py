class BookRepository:
    def __init__(self):
        self.books = [
            {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
            {"id": 2, "title": "Python Crash Course", "author": "Eric Matthes"},
            {"id": 3, "title": "Learning Python", "author": "Mark Lutz"},
        ]

    def get_all(self):
        return self.books

    def get_by_id(self, book_id: int):
        for book in self.books:
            if book["id"] == book_id:
                return book

        return None

    def create(self, title: str, author: str):
        new_id = max(
            (book["id"] for book in self.books),
            default=0
        ) + 1

        new_book = {
            "id": new_id,
            "title": title,
            "author": author
        }

        self.books.append(new_book)
        return new_book