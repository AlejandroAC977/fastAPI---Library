from app.repositories.sql_book_repository import SqlBookRepository

def test_get_all_return_all_books(tmp_path):
    db_path = str(tmp_path / "test_library.db")
    repository = SqlBookRepository(db_path)

    repository.create("Clean Code", "Robert C. Martin")
    repository.create("Python Crash Course", "Eric Matthes")

    books = repository.get_all()

    assert len(books) == 2
    assert books[0]["title"] == "Clean Code"
    assert books[1]["title"] == "Python Crash Course"

def test_get_by_id_returns_existing_book(tmp_path):
    db_path = str(tmp_path / "test_library.db")
    repository = SqlBookRepository(db_path)

    created_book = repository.create(
        "Clean Code",
        "Robert C. Martin"
    )

    book = repository.get_by_id(created_book["id"])

    assert book is not None
    assert book["title"] == "Clean Code"


def test_get_by_id_returns_none_when_not_found(tmp_path):
    db_path = str(tmp_path / "test_library.db")
    repository = SqlBookRepository(db_path)

    book = repository.get_by_id(99)

    assert book is None


def test_create_inserts_book(tmp_path):
    db_path = str(tmp_path / "test_library.db")
    repository = SqlBookRepository(db_path)

    new_book = repository.create(
        "Fluent Python",
        "Luciano Ramalho"
    )

    assert new_book["id"] == 1
    assert new_book["title"] == "Fluent Python"
    assert new_book["author"] == "Luciano Ramalho"


def test_database_persists_data(tmp_path):
    db_path = str(tmp_path / "test_library.db")

    repository = SqlBookRepository(db_path)

    created_book = repository.create(
        "Learning Python",
        "Mark Lutz"
    )

    # Creamos una segunda instancia con la misma ruta.
    second_repository = SqlBookRepository(db_path)

    book = second_repository.get_by_id(created_book["id"])

    assert book is not None
    assert book["title"] == "Learning Python"

