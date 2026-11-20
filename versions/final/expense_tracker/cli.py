import sys
from expense_tracker import storage, calculator
from expense_tracker.models import Expense


def main(argv):
    expenses = storage.load()
    if len(argv) >= 2 and argv[1] == "add":
        try:
            calculator.validate_expense(argv[2], float(argv[3]), argv[4])
        except ValueError as err:
            print(f"error: {err}", file=sys.stderr)
            sys.exit(1)
        e = Expense(argv[2], float(argv[3]), argv[4])
        expenses.append(e)
        storage.save(expenses)
        print("added", calculator.expense_label(e))
    elif len(argv) >= 2 and argv[1] == "list":
        for e in expenses:
            print(calculator.expense_label(e), round(calculator.expense_total(e), 2))
    elif len(argv) >= 2 and argv[1] == "report":
        print("total:", round(calculator.total(expenses), 2))
        print("average:", round(calculator.average(expenses), 2))
    else:
        print("usage: python -m expense_tracker.cli add <desc> <amount> <category> | list | report")


if __name__ == "__main__":
    main(sys.argv)
