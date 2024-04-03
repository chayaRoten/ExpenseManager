from http.client import HTTPException

from fastapi import APIRouter
from pydantic import ValidationError

from app.services import user_CRUD
from app.models.user import User

user_router = APIRouter()


@user_router.post('/login')
async def login(user: User):
    try:
        myUser = user_CRUD.login(user)
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred in login")
    return f"{myUser['name']} login"


@user_router.post('/sighUp')
async def sighUp(user: User):
    try:
        await user_CRUD.sighUp(user)
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred in sighUp")
    return "sighUp!!"


@user_router.put('')
async def updateUser(user: User):
    try:
        await user_CRUD.updateUser(user)
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred in updateUser")
    return "wow! update sucssesfully!!"