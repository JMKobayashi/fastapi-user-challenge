from sqlalchemy.orm import Session
from fastapi import HTTPException

from datetime import date

from . import models, schemas


def get_user_role(user_id: int, db: Session):
    user = db.query(
        models.Users, models.Roles
    ).filter_by(id=user_id).join(
        models.Roles, models.Users.role_id == models.Roles.id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"role_id": user.Roles.id, "description": user.Roles.description}


def create_user(user: schemas.User, db: Session):
    db_user = models.Users(**user.dict())
    db_user.created_at = date.today()
    db_user.updated_at = date.today()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
