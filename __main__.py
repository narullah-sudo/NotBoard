from fastapi import FastAPI
from configs import Base
import uvicorn
from routers import auth_router

app = FastAPI()

Base.metadata.drop_all(sync_engine)
Base.metadata.create_all(sync_engine)

app.include_router(auth_router)



if __name__ == '__main__':
    uvicorn.run('__main__:app', reload = True)

#http://127.0.0.1:8000/docs