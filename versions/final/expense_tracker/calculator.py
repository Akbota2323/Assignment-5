import math

from expense_tracker.models import Expense


# Single source of truth for per-category behavior.
# To add a category, add one line here.
CATEGORY_RULES: dict[str, tuple[float, str]] = {
    "food": (1.05, "FOOD"),
    "transport": (1.12, "TRANSPORT"),
    "entertainment": (1.20, "FUN"),
}
DEFAULT_RULE = (1.0, "OTHER")
VALID_CATEGORIES = set(CATEGORY_RULES) | {"other"}


def validate_expense(description: str, amount: float, category: str) -> None:
    """Raise ValueError if the expense input is not acceptable."""
    if not description.strip():
        raise ValueError("description must not be empty")
    if not math.isfinite(amount) or amount <= 0:
        raise ValueError("amount must be a positive number")
    if category not in VALID_CATEGORIES:
        raise ValueError(
            f"unknown category '{category}', use one of: {', '.join(sorted(VALID_CATEGORIES))}"
        )


def expense_total(e: Expense) -> float:
    """Return amount including category tax."""
    multiplier, _ = CATEGORY_RULES.get(e.category, DEFAULT_RULE)
    return e.amount * multiplier


def expense_label(e: Expense) -> str:
    _, tag = CATEGORY_RULES.get(e.category, DEFAULT_RULE)
    return f"[{tag}] {e.description}"


def total(expenses: list[Expense]) -> float:
    return sum(expense_total(e) for e in expenses)


def average(expenses: list[Expense]) -> float:
    if not expenses:
        return 0.0
    return total(expenses) / len(expenses)
