import pytest
from expense_tracker.calculator import expense_label, expense_total
from expense_tracker.models import Expense


@pytest.mark.parametrize("category,multiplier,label", [
    ("food", 1.05, "[FOOD] x"),
    ("transport", 1.12, "[TRANSPORT] x"),
    ("entertainment", 1.20, "[FUN] x"),
    ("other", 1.0, "[OTHER] x"),
    ("unknown-category", 1.0, "[OTHER] x"),
])
def test_category_behavior(category, multiplier, label):
    e = Expense("x", 100, category)
    assert expense_total(e) == 100 * multiplier
    assert expense_label(e) == label
