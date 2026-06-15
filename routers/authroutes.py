
from Schemas import UserSchema, UserAddSchema, UserLoginSchema
from models import User, UserSession
from configs import async_session, sync_engine, Base
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import APIRouter, Response, Cookie, Request
import token
from services import DBManagerDep, security, session_man
from typing import Annotated




auth_router = APIRouter(prefix="/auth", tags=["session"])

def _set_cookie(response: Response, token: str):
    response.set_cookie(
    key = "SessionCookie",
    value = token,
    max_age = 3600,
    path = '/',
    secure = False,
    httponly=True,
    samesite='Lax'
    )

def _clear_cookie(response: Response):
    response.delete_cookie(key = "SessionCookie")

@auth_router.post("/registration", summary="Регистрация")
async def registration_endpoint(data: UserSchema, db: DBManagerDep): 
    if await db.user.get_user_by_email(email=data.email) or await db.user.get_user_by_name(name=data.name):
        return "Error"
    new_user = User(name = data.name, email = data.email, password = security._password_hash(data.password))
    async with async_session() as session:
        session.add(new_user)
        await session.commit()

@auth_router.post("/Login", summary="Вход в аккаунт")
async def Login_user(data: UserLoginSchema,response: Response, db: DBManagerDep, request: Request) -> None:

    user = await db.user.get_user_by_name(name=data.name)
    if not user: return "Error1"
    if not security.check_password(data.password, user.password): return "Error2"
    sessionID = request.cookies.get("SessionCookie")
    if sessionID: return "Error3"
    old_session = user.session
    if old_session:await db.auth.delete_session_by_name(name = data.name)
    raw_token, token_hash = session_man.create_session_token()
    _set_cookie(response=response, token = raw_token)
    user.session = UserSession(token_hash = token_hash)
    await db.auth.create_session(user.session)

@auth_router.delete("/Logout", summary="Выход из аккаунта")
async def Logout_user(request: Request, response: Response, db: DBManagerDep) -> None:
    sessionID = request.cookies.get("SessionCookie")
    if not sessionID: return None
    token_hash = session_man.hash_token(sessionID)
    _clear_cookie(response=response)
    session_obj = await db.auth.get_session_by_token(token_hash=token_hash)
    await db.auth.delete_session(session_obj=session_obj)

    