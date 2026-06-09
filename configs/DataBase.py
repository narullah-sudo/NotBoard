from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from configs.config import get_env_settings

env = get_env_settings()

#creating sync and async engine and session 
sync_url = f"postgresql+psycopg://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DB_NAME}"
async_url= f"postgresql+asyncpg://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DB_NAME}"

sync_engine = create_engine(
    url = sync_url, echo = env.DEBUG_MODE
)
async_engine=create_async_engine(
    url=async_url,echo=env.DEBUG_MODE
)

sync_session = sessionmaker(
    bind = sync_engine, expire_on_commit = False
)
async_session=async_sessionmaker(   
    bind=async_engine,expire_on_commit=False
)

#creating Base class for tables

class Base(DeclarativeBase):
    pass

