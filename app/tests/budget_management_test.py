import pytest
from app.services import budget_management_CRUD as budgetFunc
from app.models.budget_management import Budget_Management as Budget


def sss(x):
    return x


# @pytest.mark.skip(reason='Not implemented yet')
# @pytest.mark.int
def test_add():
     # b.revenues = 700
     # b.userId = 7410
     # b.expenses = 78787
     b = {"userId": 999, "expenses": 700, "revenues": 600}
     assert budgetFunc.addToBudget(b) == "addToBudget"


def test_hh():
    assert sss(78) == 78
