from pydantic import BaseModel

class Budget_Management(BaseModel):
    revenues: int
    expenses: int
    userId: int
