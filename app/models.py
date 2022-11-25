from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    role_id = Column(Integer, ForeignKey("roles.id"))

    roles = relationship("Roles", back_populates="user_role")
    user_claims = relationship("UserClaims", back_populates="user")

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String)

    user_role = relationship("Users", back_populates='roles')

class UserClaims(Base):
    __tablename__ = "user_claims"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"), primary_key=True)

    user = relationship("Users", back_populates="user_claims")
    claim = relationship("Claims", back_populates="claim_user")

class Claims(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String)
    active = Column(Boolean)

    claim_user = relationship("UserClaims", back_populates='claim')
