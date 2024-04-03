from app.models.budget_management import Budget_Management as Budget
from app.services.db import budget_management


async def getBudget(userId):
    budget = budget_management.find_one({"userId": int(userId)})
    return budget


async def addToBudget(budget: Budget):
    budget_management.insert_one({"userId": budget.userId, "expenses": budget.expenses, "revenues": budget.revenues})
    return "addToBudget!"


async def updateBudget(budget: Budget):
    filter = {'userId': budget.userId}
    newvalues = {"$set": {"expenses": budget.expenses, "revenues": budget.revenues}}
    budget_management.update_one(filter, newvalues)
    return "updateBudget!"


async def deleteBudget(userId):
    budget_management.delete_one({"userId": int(userId)})
    return "deleteBudget"
