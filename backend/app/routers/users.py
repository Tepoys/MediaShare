from fastapi import APIRouter

userRouter = APIRouter(
    prefix="/users",
    tags=["users"],
)


@userRouter.get("/")
async def get_users():
    return {404: {"description": "Not found"}}
