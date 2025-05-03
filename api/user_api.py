# api/user_api.py

from fastapi import APIRouter, HTTPException
from services.user_service import UserService
from repositories import UserRepository
from models import User

router = APIRouter(prefix="/api/users", tags=["Users"])
user_service = UserService(UserRepository())


@router.post("/", response_model=User)
def create_user(name: str):
    return user_service.create_user(name)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    try:
        return user_service.get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
