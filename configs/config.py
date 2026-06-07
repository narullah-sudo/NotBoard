from functools import lru_cache
import os

from pydantic_settings import (BaseSettings,SettingsConfigDict)


@lru_cache
def get_env_file():
    runtime = os.getenv("ENV")
    return f".env.{runtime}" if runtime else ".env"


class ConfigBase(BaseSettings):
    DB_NAME:str
    DB_USER:str
    DB_PORT:int
    DB_HOST:str
    DEBUG_MODE:bool

    model_config = SettingsConfigDict(env_file = get_env_file(), env_file_encoding = "utf-8", extra="ignore")


@lru_cache
def get_env_settings():
    return ConfigBase()