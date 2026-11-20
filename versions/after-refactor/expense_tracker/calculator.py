from expense_tracker.models import Expense


# Single source of truth for per-category behavior.
# To add a category, add one line here.
CATEGORY_RULES: dict[str, tuple[float, str]] = {
    "food": (1.05, "FOOD"),
    "transport": (1.12, "TRANSPORT"),
    "entertainment": (1.20, "FUN"),
}
DEFAULT_RULE = (1.0, "OTHER")


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
    return total(expenses) / len(expenses)
