from fastapi import APIRouter , HTTPException
from pydantic import ValidationError
from app.log import log
from app.services import budget_management_CRUD
from app.models.budget_management import Budget_Management as Budget

budget_management_router = APIRouter()

# @log
@budget_management_router.get('')
async def getBudget(userId):
    """Routing that allows the user to access details about their expenses and revenues"""
    try:
        newBudget = await budget_management_CRUD.getBudget(userId)
        return {"userId": newBudget['userId'], "revenues": newBudget['revenues'], "expenses": newBudget['expenses']}
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in getBudget")


@budget_management_router.post('')
async def addBudget(budget: Budget):
    """Routing that enables adding expenses and revenues for a specific user"""
    try:
        await budget_management_CRUD.addToBudget(budget)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in addBudget")
    return "addBudget"



@budget_management_router.put('')
async def updateBudget(budget: Budget):
    """Routing that allows editing expenses and revenues for a specific user"""
    try:
        await budget_management_CRUD.updateBudget(budget)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in updateUser")
    return "updateBudget"


@budget_management_router.delete('')
async def deleteBudget(userId):
    """Routing that enables deleting expenses and revenues for a specific user"""
    try:
        await budget_management_CRUD.deleteBudget(userId)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in deleteBudget")
    return "deleteBudget"
