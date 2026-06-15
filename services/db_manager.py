
from fastapi import Depends
from typing import Callable, Annotated
from configs import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from .Repositories import UserRepository, AuthRepository



class DBManager:
    
    def __init__(self, session_factory: Callable[[], AsyncSession] = async_session):
        self.session_factory = session_factory
        self.session: AsyncSession | None = None
        self.user: UserRepository | None = None
        self.auth: AuthRepository | None = None
    
    async def __aenter__(self) -> "DBManager":
        self.session = self.session_factory()
        self.user = UserRepository(self.session)
        self.auth = AuthRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        if self.session:
            await self.session.close()
            

    async def commit(self) -> None:
        if self.session:
            await self.session.commit()


async def get_db_manager() -> DBManager:
    async with DBManager() as manage:
        yield manage

DBManagerDep = Annotated[DBManager, Depends(get_db_manager)]