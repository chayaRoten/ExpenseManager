from app.models.budget_management import Budget_Management as Budget
from app.services.db import budget_management as management


async def getBudget(userId):
    try:
        budget = management.find_one({"userId": int(userId)})
        return budget
    except:
        raise "error!!"


async def addToBudget(budget: Budget):
    myID = management.find_one({"userId": budget.userId})
    if myID != None:
        management.insert_one({"userId": budget.userId, "expenses": budget.expenses, "revenues": budget.revenues})
        return "addToBudget!"
    else:
        raise "id error!!!"


async def updateBudget(budget: Budget):
    myID = management.find_one({"userId": budget.userId})
    if myID != None:
        filter = {'userId': budget.userId}
        newvalues = {"$set": {"expenses": budget.expenses, "revenues": budget.revenues}}
        management.update_one(filter, newvalues)
        return "updateBudget!"
    else:
        raise "id error!!!"


async def deleteBudget(userId):
    try:
        management.delete_one({"userId": int(userId)})
        return "deleteBudget"
    except:
        raise "error!!"
