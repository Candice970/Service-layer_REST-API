# main.py

from fastapi import FastAPI
from api import book_api, user_api, order_api

app = FastAPI(
    title="Smart Inventory API",
    version="1.0.0",
    description="REST API for managing book inventory and borrowing"
)

app.include_router(book_api.router)
app.include_router(user_api.router)
app.include_router(order_api.router)
