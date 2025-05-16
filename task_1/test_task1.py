import sys

import pytest
from task1 import main, sort_list


def test_sort_list():
    assert sort_list([]) == []
    assert sort_list([5]) == [5]
    assert sort_list([3, 1, 4, 1, 5, 9, 2]) == [1, 1, 2, 3, 4, 5, 9]

    assert sort_list([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert sort_list([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert sort_list([-3, -1, -2]) == [-3, -2, -1]
    assert sort_list([2, 2, 2]) == [2, 2, 2]


@pytest.mark.parametrize("input_data,expected_output", [
    ("5 3 8 1 2", {
        "evens": [8, 2],
        "max": 8,
        "min": 1,
        "sorted": [1, 2, 3, 5, 8]
    }),
    ("7", {
        "evens": [],
        "max": 7,
        "min": 7,
        "sorted": [7]
    }),
    ("2 4 6 8", {
        "evens": [2, 4, 6, 8],
        "max": 8,
        "min": 2,
        "sorted": [2, 4, 6, 8]
    }),
    ("1 3 5 7", {
        "evens": [],
        "max": 7,
        "min": 1,
        "sorted": [1, 3, 5, 7]
    }),
    ("1000000 999999 1000001", {
        "evens": [1000000],
        "max": 1000001,
        "min": 999999,
        "sorted": [999999, 1000000, 1000001]
    }),
    ("-2 -4 -6", {
        "evens": [-2, -4, -6],
        "max": -2,
        "min": -6,
        "sorted": [-6, -4, -2]
    }),
    ("", {
        "evens": [],
        "sorted": []
    }),
])
def test_main_functionality(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr('builtins.input', lambda: input_data)
    main()
    captured = capsys.readouterr()

    if expected_output["evens"]:
        assert f"Четные числа: {expected_output['evens']}" in captured.out
    else:
        assert "Четные числа: []" in captured.out

    if "max" in expected_output:
        assert f"Максимальное число: {expected_output['max']}" in captured.out
        assert f"Минимальное число: {expected_output['min']}" in captured.out

    assert f"Отсортированный список: {expected_output['sorted']}" in captured.out


def test_main_with_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda: "1 two 3")
    main()
    captured = capsys.readouterr()
    assert "Четные числа: []" in captured.out
    assert "Отсортированный список: []" in captured.out


def test_main_with_only_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda: "abc xyz")
    main()
    captured = capsys.readouterr()
    assert "Четные числа: []" in captured.out
    assert "Отсортированный список: []" in captured.out


@pytest.mark.parametrize("input_data,expected_output", [
    (f"{sys.maxsize} {-sys.maxsize - 1}", {
        "max": sys.maxsize,
        "min": -sys.maxsize - 1,
    }),
], ids=["system_limits"])
def test_system_limits(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr('builtins.input', lambda: input_data)
    main()
    captured = capsys.readouterr()
    assert str(expected_output["max"]) in captured.out
    assert str(expected_output["min"]) in captured.out
