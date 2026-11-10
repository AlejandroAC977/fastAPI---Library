from fastapi import APIRouter, HTTPException, Depends
from app.schemas.books import BookCreate, BookResponse
from app.dependencies import get_book_service
from app.services.BookService import BookService

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("/", response_model=list[BookResponse])
def get_books(title: str | None = None, service: BookService =  Depends(get_book_service)):
    return service.get_books(title)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, service: BookService =  Depends(get_book_service)):
    book = service.get_book(book_id)
    if book is None:
        raise HTTPException(status_code= 404, detail=f"Book with id {book_id} not foud!")

    return book

@router.post("/", response_model=BookResponse, status_code=201)
def crate_book(book: BookCreate, service: BookService =  Depends(get_book_service)):
    return service.create_book(book)