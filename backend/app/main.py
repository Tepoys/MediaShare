from fastapi import FastAPI
from app.routers.users import userRouter

app = FastAPI()

app.include_router(userRouter)
