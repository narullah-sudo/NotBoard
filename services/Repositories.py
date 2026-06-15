
from sqlalchemy import select
from  sqlalchemy.orm import selectinload
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, UserSession
from .sessions import session_man

class UserRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_name(self, name: str) -> Optional["User"]:
        user = await self.session.scalar(select(User).where(User.name == name).options(selectinload(User.session)))
        return user


    async def get_user_by_email(self, email: str) -> Optional["User"]:
        return await self.session.scalar(select(User).where(User.email == email))


    async def get_user_by_id(self, id: int) -> Optional["User"]:
        return await self.session.scalar(select(User).where(User.id == id))

    async def create_user(self, name: str, email: str, password: str) -> None:
        user = User(name = name, email = eamil, password = password)
        self.session.add(user)
        await self.session.commit()


class AuthRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_session_by_token(self, token_hash: str) -> Optional[UserSession]:
        return await self.session.scalar(select(UserSession).where(UserSession.token_hash == token_hash).options(selectinload(UserSession.user)))

    async def delete_session(self, session_obj: UserSession) -> None:
        await self.session.delete(session_obj)
        await self.session.commit()

    async def delete_session_by_name(self, name: str) -> None:
        session_user = await self.session.scalar(select(User).where(User.name == name))
        self.delete_session(session_obj=session_user)

    async def get_user_by_session(self, session_id: str) -> Optional[User]:
        token_hash = session_man.hash_token(session_id)
        session = await self.get_session_by_token(token_hash=token_hash)
        return session.user

    async def create_session(self, session_obj: UserSession) -> None:
        self.session.add(session_obj)
        await self.session.commit()


    