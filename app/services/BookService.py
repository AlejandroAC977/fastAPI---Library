from app.schemas.books import BookCreate
from app.repositories.book_repository import BookRepository

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_books(self, title: str | None = None):
        books = self.repository.get_all()
        
        if title:
            return[
                book for book in books
                if title.lower() in book["title"].lower()
            ]
        
        return books

    def get_book(self, book_id: int):
        return self.repository.get_by_id(book_id)

    def create_book(self, book: BookCreate):
        
        return self.repository.create(
            title=book.title,
            author=book.author
        )