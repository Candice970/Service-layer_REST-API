# services/order_service.py

from repositories import OrderRepository, BookRepository, UserRepository
from models import Order
from uuid import uuid4


class OrderService:
    def __init__(self, order_repo: OrderRepository, book_repo: BookRepository, user_repo: UserRepository):
        self.order_repo = order_repo
        self.book_repo = book_repo
        self.user_repo = user_repo

    def create_order(self, user_id: str, book_ids: list) -> Order:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found.")
        if len(user.borrowed_books) + len(book_ids) > 5:
            raise ValueError("User cannot borrow more than 5 books.")

        for book_id in book_ids:
            book = self.book_repo.find_by_id(book_id)
            if not book or book.checked_out:
                raise ValueError(f"Book {book_id} is unavailable.")
            book.checked_out = True
            self.book_repo.save(book)
            user.borrowed_books.append(book_id)

        self.user_repo.save(user)

        order = Order(id=str(uuid4()), user_id=user_id, book_ids=book_ids)
        return self.order_repo.save(order)
