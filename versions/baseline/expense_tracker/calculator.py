from expense_tracker.models import Expense


def expense_total(e: Expense) -> float:
    """Return amount including category tax/discount."""
    if e.category == "food":
        return e.amount * 1.05
    elif e.category == "transport":
        return e.amount * 1.12
    elif e.category == "entertainment":
        return e.amount * 1.20
    else:
        return e.amount


def expense_label(e: Expense) -> str:
    if e.category == "food":
        return f"[FOOD] {e.description}"
    elif e.category == "transport":
        return f"[TRANSPORT] {e.description}"
    elif e.category == "entertainment":
        return f"[FUN] {e.description}"
    else:
        return f"[OTHER] {e.description}"


def total(expenses: list[Expense]) -> float:
    return sum(expense_total(e) for e in expenses)


def average(expenses: list[Expense]) -> float:
    return total(expenses) / len(expenses)
