from unittest.mock import patch

import pandas as pd

from src.csv_pandas import read_from_csv, read_from_excel


@patch("pandas.read_csv")
def test_read_from_csv(mock_pd_read_csv):
    """Функция, тестирующая функцию чтения данных из CSV-файла"""
    mock_pd_read_csv.return_value = pd.DataFrame({"ID": ["50"], "state": ["EXECUTED"]})
    assert read_from_csv("id,state\\n50,EXECUTED") == [{"ID": "50", "state": "EXECUTED"}]


def test_2_read_from_csv():
    """Функция, тестирующая функцию чтения данных из CSV-файла с неккоректным путём к файлу."""
    assert read_from_csv("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\transaction") == []


@patch("pandas.read_excel")
def test_read_from_excel(mock_read_excel):
    """Функция, тестирующая функцию чтения данных из excel-файла."""
    mock_read_excel.return_value = pd.DataFrame({"ID": ["50"], "state": ["EXECUTED"]})
    assert read_from_excel("id,state\\n50,EXECUTED") == [{"ID": "50", "state": "EXECUTED"}]


def test_2_read_from_excel():
    """Функция, тестирующая функцию чтения данных из excel-файла с неккоректным путём к файлу"""
    assert read_from_excel("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\transaction") == []
