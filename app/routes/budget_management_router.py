from fastapi import APIRouter, HTTPException
from app.services import budget_management_CRUD
from app.models.budget_management import budget_Management as Budget

budget_management_router = APIRouter()


@budget_management_router.get('')
async def get_budget():
    """Routing that allows the user to access details about their expenses and revenues"""
    try:
        budgets = await budget_management_CRUD.get_budget()
        s = ""
        for i in budgets:
            s += "expenses: "
            s += (str(i['expenses']))
            s += " revenues: "
            s += (str(i['revenues']))
            s += " userId: "
            s += (str(i['userId']))
            s += " id: "
            s += (str(i['id']))
            s += " date: "
            s += (str(i['date']))
            s += ", "
        return s
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in getBudget")


@budget_management_router.post('')
async def add_budget(budget: Budget):
    """Routing that enables adding expenses and revenues for a specific user"""
    try:
        await budget_management_CRUD.add_to_budget(budget)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in addBudget")
    return "addBudget"


@budget_management_router.put('')
async def update_budget(budget: Budget):
    """Routing that allows editing expenses and revenues for a specific user"""
    try:
        await budget_management_CRUD.update_budget(budget)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in updateUser")
    return "updateBudget"


@budget_management_router.delete('')
async def delete_budget(id):
    """Routing that allows editing expenses and revenues for a specific user"""
    try:
        await budget_management_CRUD.delete_budget(id)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error occurred in deleteBudget")
    return "deleteBudget"
