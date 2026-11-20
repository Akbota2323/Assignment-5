from expense_tracker.calculator import expense_total, total
from expense_tracker.models import Expense


def test_food_tax():
    assert round(expense_total(Expense("lunch", 100, "food")), 2) == 105.0


def test_other_no_tax():
    assert expense_total(Expense("misc", 50, "other")) == 50


def test_total_sums_all():
    items = [Expense("a", 100, "food"), Expense("b", 100, "other")]
    assert round(total(items), 2) == 205.0
