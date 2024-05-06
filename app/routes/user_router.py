from fastapi import APIRouter , HTTPException
from pydantic import ValidationError
from app.services import user_CRUD
from app.models.user import User

user_router = APIRouter()


@user_router.post('/login')
async def login(user: User):
    """Routing that allows an existing user to log in to the system"""
    try:
        myUser = user_CRUD.login(user)
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred in login")
    return f"{myUser['name']} login"


@user_router.post('/sighUp')
async def sighUp(user: User):
    """Routing that allows a new user to register for the system"""
    try:
        await user_CRUD.sighUp(user)
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred in sighUp")
    return "sighUp!!"


@user_router.put('')
async def updateUser(user: User):
    """Routing that enables editing details of a specific user"""
    try:
        await user_CRUD.updateUser(user)
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred in updateUser")
    return "wow! update sucssesfully!!"