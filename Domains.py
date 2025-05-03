# models.py

from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4


class Book(BaseModel):
    id: str
    title: str
    author: str
    checked_out: bool = False


class User(BaseModel):
    id: str
    name: str
    borrowed_books: List[str] = []


class Order(BaseModel):
    id: str
    user_id: str
    book_ids: List[str]
