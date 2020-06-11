from fastapi import HTTPException


def get_users():
    users = [{"name": "foo", "email": "1"}, {"name": "bar", "email": "2"}]
    return users


def create_user(email):
    if email == "baz@baz.com":
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
