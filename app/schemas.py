from typing import List, Optional

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    role_id: int
    password: Optional[str] = ""
    
    class Config:
        orm_mode = True

class UserDescription(BaseModel):
    name: str
    email: str
    role_description: str
    claim_description: str

    class Config:
        orm_mode = True