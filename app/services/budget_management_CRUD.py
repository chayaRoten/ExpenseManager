from app.log import log
from app.models.budget_management import budget_Management as Budget
from app.services.db import budget_management as management
from app.services import user_CRUD

user_id = -1


@log("logs.txt")
async def get_budget():
    """Receiving a report of expenses and revenues for a specific user"""
    try:
        global user_id
        budgets = []
        user_id = user_CRUD.user_id
        for document in management.find({"userId": int(user_id)}):
            budgets.append(document)
        return budgets
    except Exception:
        raise "error!!"


@log("logs.txt")
async def add_to_budget(budget: Budget):
    """Adding expenses and revenues of a specific user to the management system"""
    try:
        management.insert_one(
            {"userId": user_CRUD.user_id, "expenses": budget.expenses, "revenues": budget.revenues,
             "id": budget.id, "date": budget.date})
        return "addToBudget!"
    except Exception:
        raise "user id error!!!"


@log("logs.txt")
async def update_budget(budget: Budget):
    """Managing expenses and revenues for a specific user"""
    try:
        my_filter = management.find_one({'id': budget.id})
        new_values = {
            "$set": {"expenses": budget.expenses, "revenues": budget.revenues, "id": budget.id,
                     "date": budget.date}}
        management.update_one(my_filter, new_values)
        return "updateBudget!"
    except Exception:
        raise "id error!!!"


@log("logs.txt")
async def delete_budget(id):
    """Deleting expenses and revenues for a specific user"""
    try:
        management.delete_one({"id": int(id)})
        return "deleteBudget!"
    except Exception:
        raise "error!!"
