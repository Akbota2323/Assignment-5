from expense_tracker.calculator import average, total


def test_average_empty_is_zero():
    assert average([]) == 0.0


def test_total_empty_is_zero():
    assert total([]) == 0
