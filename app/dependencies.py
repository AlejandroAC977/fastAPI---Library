from fastapi import Depends
from app.interfaces.book_repository_protocol import BookRepositoryProtocol
from app.repositories.sql_book_repository import SqlBookRepository
from app.services.BookService import BookService

# regresa el repositorio requerido al momento
def get_book_repository()-> BookRepositoryProtocol:
    return SqlBookRepository()

# retorna el repositorio elegido y lo hace la dependencia del servicio 
def get_book_service(
    repository: BookRepositoryProtocol = Depends(get_book_repository)    
) -> BookService:
    return BookService(repository)
