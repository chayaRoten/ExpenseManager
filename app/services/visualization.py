import matplotlib.pyplot as plt
from app.services import budget_management_CRUD as budgetFunc


async def plot():
    """Retrieve the user's UserID and display for them data segmentation regarding income and expenses"""
    data = await budgetFunc.get_budget()
    revenues = []
    expenses = []
    for i in data:
        revenues.append(i['revenues'])
        expenses.append(i['expenses'])
    plt.plot(revenues, expenses, marker='o', linestyle='-')
    plt.title('Visualization of Data')
    plt.xlabel('revenues')
    plt.ylabel('expenses')
    plt.show()
    return "yes"
