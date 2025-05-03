# api/order_api.py

from fastapi import APIRouter, HTTPException
from services.order_service import OrderService
from repositories import OrderRepository, BookRepository, UserRepository
from models import Order

router = APIRouter(prefix="/api/orders", tags=["Orders"])
order_service = OrderService(OrderRepository(), BookRepository(), UserRepository())


@router.post("/", response_model=Order)
def place_order(user_id: str, book_ids: list[str]):
    try:
        return order_service.create_order(user_id, book_ids)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
