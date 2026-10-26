from fastapi import APIRouter, HTTPException
from app.schemas.books import BookCreate, BookResponse
from app.repositories.book_repository import BookRepository

from app.services.BookService import BookService

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

book_repo = BookRepository()
book_service = BookService(book_repo)

@router.get("/", response_model=list[BookResponse])
def get_books(title: str | None = None):
    return book_service.get_books(title)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    book = book_service.get_book(book_id)
    if book is None:
        raise HTTPException(status_code= 404, detail=f"Book with id {book_id} not foud!")

    return book

@router.post("/", response_model=BookResponse, status_code=201)
def crate_book(book: BookCreate):
    return book_service.create_book(book)