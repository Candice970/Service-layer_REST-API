# api/book_api.py

from fastapi import APIRouter, HTTPException
from services.book_service import BookService
from repositories import BookRepository
from models import Book

router = APIRouter(prefix="/api/books", tags=["Books"])
book_service = BookService(BookRepository())


@router.post("/", response_model=Book)
def create_book(title: str, author: str):
    return book_service.create_book(title, author)


@router.get("/", response_model=list[Book])
def list_books():
    return book_service.get_all_books()


@router.post("/{book_id}/checkout", response_model=Book)
def checkout_book(book_id: str):
    try:
        return book_service.checkout_book(book_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
