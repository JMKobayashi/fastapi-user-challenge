from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, schemas, utils
from .database import SessionLocal, engine

app = FastAPI()

utils.create_db(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/{user_id}/role", response_model=schemas.User, tags=["User"])
def read_user_role(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_role(user_id, db)


@app.post("/user/create", response_model=schemas.User, tags=["User"])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    if user.password == "":
        user.password = utils.create_random_password()

    return crud.create_user(user, db)
