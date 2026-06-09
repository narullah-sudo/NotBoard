from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from typing import Optional, List
import sys, asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from configs.DataBase import Base, sync_engine, async_engine, sync_session, async_session


class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key = True, nullable = False)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

    user_data: Mapped[Optional("UserData")] = relationship(
        "UserData",
        back_populates = 'user',
        uselist = False,
        cascade = "all, delete-orphan"
    )

class UserData(Base):
    __tablename__ = 'User_data'


    user_id: Mapped[int] = mapped_column(
        ForeignKey("Users.id"),
        primary_key = True)


    notices: Mapped[List["Notice"]] = relationship(
    "Notice",
    uselist = True,
    cascade = "all, delete-orphan",
    back_populates = "creater")


    user: Mapped[Optional("User")] = relationship(
        "User",
        back_populates = 'user_data'
    )


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




