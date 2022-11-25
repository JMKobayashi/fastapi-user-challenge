from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    role_id: int = 3
    password: Optional[str] = ""

    class Config:
        orm_mode = True


class UserCreate(User):
    id: int


class Role(BaseModel):
    role_id: int
    description: str
