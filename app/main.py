import random
import string

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/{user_id}/role", response_model=schemas.User, tags=["User"])
def read_user_role(user_id: int, db: Session = Depends(get_db)):
    """Get user role id by user id
    Return:
        {
            "name": <String>,
            "email": <String>,
            "role_id": <Integer>
        }
    Parameters:
        {user_id}: <Integer>
    """
    return crud.get_user_role(user_id, db)


@app.post("/user/create", response_model=schemas.User, tags=["User"])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    """Create new user
    Return:
        {
            "name": <String>,
            "email": <String>,
            "role_id": <Integer>,
            "password": <String>
        }
    Parameters:
        {
            "name": <String>,
            "email: <String>,
            "role_id": <Integer>,
            "password": <String|Optional>
        }
    """
    if user.password == "":
        user.password = create_random_password()

    return crud.create_user(user, db)


def create_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(9))

    return password
