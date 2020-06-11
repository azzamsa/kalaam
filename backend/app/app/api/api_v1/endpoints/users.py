from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_users():
    """
    Retrieve users.
    """
    return {"Hello": "World"}
