
from pydantic import BaseModel


class budget_Management(BaseModel):
    id: int
    date: str
    revenues: int
    expenses: int
    userId: int
