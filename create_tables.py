from app.database.connection import engine
from app.database.base import Base

from app.models.book import Book

Base.metadata.create_all(bind=engine)

print("Todas las tablas fueron creadas")