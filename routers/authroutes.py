
from Schemas import UserSchema, UserAddSchema
from models import User
from configs import async_session, sync_engine, Base
from sqlalchemy import select
from fastapi import APIRouter, Response
import token



auth_router = APIRouter()


@auth_router.post("/registration")
async def registration_endpoint(data: UserSchema):
    new_user = User(name = data.name, email = data.email, password = data.password)
    async with async_session() as session:
        stmt = select(User).where(User.email == new_user.email)
        result = await session.execute(stmt)
        user = result.scalar()
        if not user:
            session.add(new_user)
            await session.commit()
        else:
            return {"user":user, "error": "эта почта занята"}
        return user, result