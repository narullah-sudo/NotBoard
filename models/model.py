from sqlalchemy import ForeignKey, select, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from typing import Optional, List
import asyncio
from datetime import datetime


from configs import (Base, sync_engine, async_engine, sync_session, async_session)


class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key = True, nullable = False)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[bytes]

    user_data: Mapped[Optional("UserData")] = relationship("UserData",back_populates = 'user',uselist = False,cascade = "all, delete-orphan")
    session: Mapped[Optional("UserSession")] = relationship("UserSession", back_populates="user", uselist=False, cascade= "all, delete-orphan")


class UserSession(Base):
    __tablename__ = "sessions"
    session_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    token_hash: Mapped[str] 
    #expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped[Optional("User")] = relationship("User", back_populates="session")



class UserData(Base):
    __tablename__ = 'User_data'

    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"),primary_key = True)

    notices: Mapped[List["Notice"]] = relationship("Notice",uselist = True,cascade = "all, delete-orphan",back_populates = "creater")
    user: Mapped[Optional("User")] = relationship("User",back_populates = 'user_data')


class Notice(Base):
    __tablename__ = 'Notices'

    id: Mapped[int] = mapped_column(primary_key = True, nullable = False)
    creater: Mapped[Optional("UserData")] = relationship(
        "UserData",
        back_populates="notices"
    )

    creater_id: Mapped[int] = mapped_column(ForeignKey("User_data.user_id"))

    title: Mapped[str]
    image: Mapped[str]




