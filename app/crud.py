from sqlalchemy import select
from sqlalchemy.orm import Session, aliased


from datetime import date

from . import models, schemas

def get_user_role(user_id: int, db: Session):
    return db.query(models.Users).filter_by(id=user_id).first()

def create_user(user: schemas.User, db: Session):
    db_user = models.Users(**user.dict())
    db_user.created_at = date.today()
    db_user.updated_at = date.today()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user