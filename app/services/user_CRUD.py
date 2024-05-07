from app.models.user import User
from app.services.db import users


async def login(user: User):
    """The option for an existing user to log in to the system"""
    myUser = users.find_one({"name": user.name, "password": user.password})
    if myUser:
        return myUser
    return "error!"


async def signUp(user: User):
    """Adding a new user to the system"""
    users.insert_one({"name": user.name, "password": user.password, "id": user.id})
    return "sign up!"


async def updateUser(user: User):
    """Editing the details for a specific user"""
    filter = {'id': user.id}
    newvalues = {"$set": {"name": user.name, "password": user.password}}
    users.update_one(filter, newvalues)
    return "update user!"
