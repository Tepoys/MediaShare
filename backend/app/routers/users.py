from fastapi import APIRouter

router = APIRouter()


@router.get("/user/", tags=["users"])
async def get_users():
    pass
