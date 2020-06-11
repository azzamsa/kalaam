from typing import List

from app.user import schema
from app.user import service as user_service
from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=List[schema.User])
def get_users():
    """
    Retrieve users.
    """
    users = user_service.get_users()
    return users


@router.post("/", response_model=schema.User)
def create_user(
    *, user_in: schema.UserCreate,
):
    """
    Create new user.
    """
    user = user_service.create_user(email=user_in.email)
    return user
