import json
from expense_tracker.models import Expense

DB_FILE = "expenses.json"


def load() -> list[Expense]:
    try:
        with open(DB_FILE) as f:
            return [Expense(**d) for d in json.load(f)]
    except FileNotFoundError:
        return []


def save(expenses: list[Expense]) -> None:
    with open(DB_FILE, "w") as f:
        json.dump([e.__dict__ for e in expenses], f)
