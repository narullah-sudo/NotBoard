
from sqlalchemy import select
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, UserSession


class UserRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_name(self, name: str) -> Optional[User]:
        return await self.session.scalar(select(User).where(User.name == name))

    async def get_user_by_id(self, id: int) -> Optional[User]:
        return await self.session.scalar(select(User).where(User.id == id))

    async def create_user(self, name: str, email: str, password: str) -> None:
        user = User(name = name, email = eamil, password = password)


class AuthRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_session_by_token(self, token_hash: str) -> Optional[UserSession]:
        return await self.session.scalar(select(UserSession).where(UserSession.token_hash == token_hash))

    async def delete_session(self, session_obj: UserSession) -> None:
        await self.session.delete(session_obj)