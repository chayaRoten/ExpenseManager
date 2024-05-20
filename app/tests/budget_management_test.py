import asyncio
from app.services import budget_management_CRUD as budgetFunc
from app.models.budget_management import budget_Management as Budget
import unittest


class TestHH(unittest.TestCase):

    def test_addToBudget(self):
        budget = Budget(userId=11111, expenses=700, revenues=600, date='10/10/25', id='2')
        result = asyncio.run(budgetFunc.add_to_budget(budget))
        assert result == "addToBudget!"

    def test_updateToBudget(self):
        budget = Budget(userId=11111, expenses=70, revenues=60, date='10/10/25', id='2')
        result = asyncio.run(budgetFunc.update_budget(budget))
        assert result == "updateBudget!"

    def test_deleteBudget(self):
        result = asyncio.run(budgetFunc.delete_budget(11111))
        assert result == "deleteBudget!"


if __name__ == '__main__':
    unittest.main()
