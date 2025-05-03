# repositories.py

from models import Book, User, Order
from typing import Dict


class BookRepository:
    def __init__(self):
        self.books: Dict[str, Book] = {}

    def save(self, book: Book):
        self.books[book.id] = book
        return book

    def find_by_id(self, book_id: str):
        return self.books.get(book_id)

    def find_all(self):
        return list(self.books.values())


class UserRepository:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def save(self, user: User):
        self.users[user.id] = user
        return user

    def find_by_id(self, user_id: str):
        return self.users.get(user_id)


class OrderRepository:
    def __init__(self):
        self.orders: Dict[str, Order] = {}

    def save(self, order: Order):
        self.orders[order.id] = order
        return order

    def find_by_id(self, order_id: str):
        return self.orders.get(order_id)
