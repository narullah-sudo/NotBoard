from configs import Base
from fastapi import FastAPI, APIRouter
from Schemas import UserSchema, UserAddSchema
from models import User
from configs import async_session, sync_engine, Base
import uvicorn
from sqlalchemy import select
from services import auth_router
#from sqlalchemy.orm import 

app = FastAPI()
app.add_route(auth_router)

Base.metadata.drop_all(sync_engine)
Base.metadata.create_all(sync_engine)


        


if __name__ == '__main__':
    uvicorn.run('__main__:app', reload = True)
