from app.models.user import User
from app.services.db import users


def login(user: User):
    myUser = users.find_one({"name": user.name, "password": user.password})
    if myUser:
        return myUser
    return "error!"


async def sighUp(user: User):
    users.insert_one({"name": user.name, "password": user.password, "id": user.id})
    return "sigh up!"


async def updateUser(user: User):
    filter = {'id': user.id}
    newvalues = {"$set": {"name": user.name, "password": user.password}}
    users.update_one(filter, newvalues)
    return "update user!"
