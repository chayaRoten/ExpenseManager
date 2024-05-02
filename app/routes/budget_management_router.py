from http.client import HTTPException
from fastapi import APIRouter
from pydantic import ValidationError

from app.services import budget_management_CRUD
from app.models.budget_management import Budget_Management as Budget

budget_management_router = APIRouter()


@budget_management_router.get('')
async def getBudget(userId):
    newBdget = await budget_management_CRUD.getBudget(userId)
    return {"userId": newBdget['userId'], "revenues": newBdget['revenues'], "expenses": newBdget['expenses']}


@budget_management_router.post('')
async def addBudget(budget: Budget):
    try:
        await budget_management_CRUD.addToBudget(budget)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in addBudget")
    return "addBudget"


@budget_management_router.put('')
async def updateBudget(budget: Budget):
    try:
        await budget_management_CRUD.updateBudget(budget)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in updateUser")
    return "updateBudget"


@budget_management_router.delete('')
async def deleteBudget(userId):
    try:
        await budget_management_CRUD.deleteBudget(userId)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in deleteBudget")
    return "deleteBudget"
