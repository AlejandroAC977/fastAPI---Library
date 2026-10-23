from fastapi import FastAPI
from app.schemas.books import BookCreate, BookResponse
from fastapi import HTTPException
from app.routers.books import router as books_router

books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Python Crash Course", "author": "Eric Matthes"},
    {"id": 3, "title": "Learning Python", "author": "Mark Lutz"},
]

app = FastAPI()
app.include_router(books_router)

@app.get("/")
def root():
    return {"message":"Welcome to my library"}

# @app.get("/books/{book_id}", response_model=BookResponse)
# def get_book(book_id: int 
#              #books:list = books
#             ):
#     for book in books:
#         if book["id"] == book_id:
#             return book

#     raise HTTPException(
#         status_code=404,
#         detail=f"Book with id {book_id} not found"
#     )


# @app.get("/books")
# def get_books(title: str | None= None):
#     books = [
#         {
#             "id":1,
#             "title": "Clean Code",
#             "author":"Robert C. Martin"
#         },
#         {
#             "id":2,
#             "title":"Python Crash Course",
#             "author":"Eric Matthes"
#         },
#         {
#             "id": 3,
#             "title": "Learning Python",
#             "author": "Mark Lutz"
#         }
#     ]

#     if title:
#         books=[
#             book 
#             for book in books 
#             if title.lower() in book["title"].lower()
#         ]

#     return books

# @app.post("/books", response_model=BookResponse, status_code=201)
# def create_book(book: BookCreate):
#     return {
#         "id": 1,
#         "title": book.title,
#         "author": book.author 
#     }