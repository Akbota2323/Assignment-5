import math

import pytest

from expense_tracker import cli
from expense_tracker.calculator import validate_expense


def test_valid_expense_passes():
    validate_expense("lunch", 10.5, "food")


@pytest.mark.parametrize("amount", [0, -50, math.nan, math.inf])
def test_bad_amount_rejected(amount):
    with pytest.raises(ValueError):
        validate_expense("x", amount, "food")


def test_unknown_category_rejected():
    with pytest.raises(ValueError):
        validate_expense("x", 10, "transprt")


def test_empty_description_rejected():
    with pytest.raises(ValueError):
        validate_expense("  ", 10, "food")


def test_cli_rejects_bad_input_and_saves_nothing(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(SystemExit) as exc:
        cli.main(["cli", "add", "x", "-5", "food"])
    assert exc.value.code == 1
    assert "error:" in capsys.readouterr().err
    assert not (tmp_path / "expenses.json").exists()


def test_cli_report_on_empty_db(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    cli.main(["cli", "report"])
    out = capsys.readouterr().out
    assert "total: 0" in out and "average: 0.0" in out


def test_cli_add_list_roundtrip(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    cli.main(["cli", "add", "lunch", "100", "food"])
    cli.main(["cli", "list"])
    assert "[FOOD] lunch 105.0" in capsys.readouterr().out
