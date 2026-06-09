from functools import lru_cache
import os

from pydantic_settings import (BaseSettings,SettingsConfigDict)

#function for get env file path
@lru_cache
def get_env_file():
    runtime = os.getenv("ENV")
    return f".env.{runtime}" if runtime else ".env"

#class with base settings
class ConfigBase(BaseSettings):
    DB_NAME:str
    DB_USER:str
    DB_PORT:int
    DB_HOST:str
    DB_PASSWORD:str
    DEBUG_MODE:bool

    model_config = SettingsConfigDict(env_file = get_env_file(), env_file_encoding = "utf-8", extra="ignore")


#function for get class instance
@lru_cache
def get_env_settings():
    return ConfigBase()