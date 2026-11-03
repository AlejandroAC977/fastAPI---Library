from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.dependencies import get_book_repository

class FakeBookRepository:

    def __init__(self):
        self.books = [
            {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
            {"id": 2, "title": "Python Crash Course", "author": "Eric Matthes"},
            {"id": 3, "title": "Learning Python", "author": "Mark Lutz"},
        ]

    def get_all(self) -> list[dict]:
        return self.books

    def get_by_id(self, book_id: int) -> dict | None:
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def create(self, title: str, author: str) -> dict:
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

# FIXTURE: prepara el entorno de prueba
@pytest.fixture
def client():
    fake_repository = FakeBookRepository()

    def override_get_book_repository():
        return fake_repository

    app.dependency_overrides[get_book_repository] = (
        override_get_book_repository
    )

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.pop(get_book_repository, None)


# TEST 1: obtener todos los libros
def test_get_books(client):
    response = client.get("/books/")

    assert response.status_code == 200
    assert len(response.json()) == 3


# TEST 2: buscar un libro inexistente
def test_get_book_not_found(client):
    response = client.get("/books/99")

    assert response.status_code == 404


# TEST 3: crear un libro
def test_create_book(client):
    new_book = {
        "title": "Fluent Python",
        "author": "Luciano Ramalho"
    }

    response = client.post("/books/", json=new_book)

    assert response.status_code == 201
    assert response.json()["id"] == 4
    assert response.json()["title"] == "Fluent Python"

    get_response = client.get("/books/4")

    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Fluent Python"