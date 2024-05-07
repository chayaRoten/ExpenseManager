from app.log import log
from app.models.budget_management import Budget_Management as Budget
from app.services.db import budget_management as management


@log("logs.txt")
async def getBudget(userId):
    """Receiving a report of expenses and revenues for a specific user"""
    try:
        budget = management.find_one({"userId": int(userId)})
        return budget
    except:
        raise "error!!"


@log("logs.txt")
async def addToBudget(budget: Budget):
    """Adding expenses and revenues of a specific user to the management system"""
    myID = management.find_one({"userId": budget.userId})
    if myID == None:
        management.insert_one({"userId": budget.userId, "expenses": budget.expenses, "revenues": budget.revenues})
        return "addToBudget!"
    else:
        raise "id error!!!"



async def updateBudget(budget: Budget):
    """Managing expenses and revenues for a specific user"""
    myID = management.find_one({"userId": budget.userId})
    if myID != None:
        filter = {'userId': budget.userId}
        newvalues = {"$set": {"expenses": budget.expenses, "revenues": budget.revenues}}
        management.update_one(filter, newvalues)
        return "updateBudget!"
    else:
        raise "id error!!!"


async def deleteBudget(userId):
    """Deleting expenses and revenues for a specific user"""
    try:
        management.delete_one({"userId": int(userId)})
        return "deleteBudget!"
    except:
        raise "error!!"
