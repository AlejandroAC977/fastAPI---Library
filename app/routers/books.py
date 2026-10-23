from fastapi import APIRouter, HTTPException
from app.schemas.books import BookCreate, BookResponse

books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Python Crash Course", "author": "Eric Matthes"},
    {"id": 3, "title": "Learning Python", "author": "Mark Lutz"},
]

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("/", response_model=list[BookResponse])
def get_books(title: str | None = None):
    if title:
        return [
            book 
            for book in books
            if title.lower() in book["title"].lower()
        ]
    
    return books

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail=f"book with id: {book_id} not found!")

@router.post("/", response_model=BookResponse, status_code=201)
def crate_book(book: BookCreate):
    new_id = max((item["id"] for item in books), default=0) + 1
    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author
    }

    books.append(new_book)
    return new_book