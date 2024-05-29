from fastapi import APIRouter, HTTPException
from app.services import user_CRUD
from app.models.user import User

user_router = APIRouter()


@user_router.post('/login')
async def login(user: User):
    """Routing that allows an existing user to log in to the system"""
    try:
        my_user = await user_CRUD.login(user)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in login")
    return f"{my_user['name']} login"


@user_router.post('/signUp')
async def sign_up(user: User):
    """Routing that allows a new user to register for the system"""
    try:
        await user_CRUD.sign_up(user)
    except Exception:
        raise HTTPException(status_code=400, detail=f"oops... an error occurred in signUp")
    return "sighUp!!"


@user_router.put('')
async def update_user(user: User):
    """Routing that enables editing details of a specific user"""
    try:
        await user_CRUD.update_user(user)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in updateUser")
    return "wow! update successfully!!"
