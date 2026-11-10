from app.schemas.books import BookCreate
from app.services.BookService import BookService

class FakeRepository:
    def __init__(self):
        self.books = [
            {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
            {"id": 2, "title": "Python Crash Course", "author": "Eric Matthes"},
            {"id": 3, "title": "Learning Python", "author": "Mark Lutz"},
        ]

    def get_all(self):
        return self.books

    def get_by_id(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def create(self, title, author):
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

def test_get_books_return_all_books():
    service = BookService(FakeRepository())

    books = service.get_books()

    assert len(books) == 3

def test_get_books_filters_by_title():
    service = BookService(FakeRepository())

    books = service.get_books(title="python")

    assert len(books) == 2
    assert all("python" in book["title"].lower() for book in books)
    

def test_get_book_return_exiting_book():
    service = BookService(FakeRepository())

    book = service.get_book(2)

    assert book is not None
    assert book["title"] == "Python Crash Course"


def test_get_book_returns_none_when_not_found():
    service = BookService(FakeRepository())

    book = service.get_book(99)

    assert book is None

def test_create_book():
    service = BookService(FakeRepository())

    book_data = BookCreate(
        title="Fluent Python",
        author="Luciano Ramalho"
    )

    new_book = service.create_book(book_data)

    assert new_book["id"] == 4
    assert new_book["title"] == "Fluent Python"
    assert new_book["author"] == "Luciano Ramalho"