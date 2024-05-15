import requests
import matplotlib.pyplot as plt
from app.services import budget_management_CRUD as budgetFunc
from app.services import user_CRUD as userFunc


async def plot():
    data = await budgetFunc.getBudget(userFunc.user_id)
    plt.plot(data['revenues'], data['expenses'], marker='o', linestyle='-')
    plt.title('Visualization of Data')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
    return "yes"
