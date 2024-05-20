from app.models.user import User
from app.services.db import users
from app.log import log

user_id = None


@log("logs.txt")
async def login(user: User):
    """The option for an existing user to log in to the system"""
    global user_id
    my_user = users.find_one({"name": user.name, "password": user.password})
    if my_user:
        user_id = my_user['id']
        return my_user
    return "error!"


@log("logs.txt")
async def sign_up(user: User):
    """Adding a new user to the system"""
    users.insert_one({"name": user.name, "password": user.password, "id": user.id})
    global user_id
    user_id = user.id
    return "sign up!"


@log("logs.txt")
async def update_user(user: User):
    """Editing the details for a specific user"""
    my_filter = {'id': user.id}
    new_values = {"$set": {"name": user.name, "password": user.password}}
    users.update_one(my_filter, new_values)
    return "update user!"
