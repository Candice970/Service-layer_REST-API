# services/user_service.py

from repositories import UserRepository
from models import User
from uuid import uuid4


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, name: str) -> User:
        user = User(id=str(uuid4()), name=name)
        return self.user_repo.save(user)

    def get_user(self, user_id: str) -> User:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found.")
        return user
