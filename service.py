# services/book_service.py

from repositories import BookRepository
from models import Book
from uuid import uuid4


class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def create_book(self, title: str, author: str) -> Book:
        book = Book(id=str(uuid4()), title=title, author=author)
        return self.book_repo.save(book)

    def checkout_book(self, book_id: str) -> Book:
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise ValueError("Book not found.")
        if book.checked_out:
            raise ValueError("Book already checked out.")
        book.checked_out = True
        return self.book_repo.save(book)

    def get_all_books(self):
        return self.book_repo.find_all()
