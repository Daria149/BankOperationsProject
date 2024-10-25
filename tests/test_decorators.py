import pytest
from src.decorators import log, result_function


def test_log_func():
    @log("")
    def result_function(x, y):
        return x ** y

    result = result_function(2, 3)
    assert result == 8


def test_2_log_func():
    with pytest.raises(Exception):
        result_function()


def test_3_log_func():
    @log("func_log.txt")
    def result_function(x, y):
        return x ** y

    result = result_function(1, 5)
    assert result == 1


def test_4_log_func(capsys):
    @log()
    def result_function(x, y):
        return x ** y

    result = result_function(2, 1)
    captured = capsys.readouterr()
    assert result == 2
    assert captured.out
