from unittest.mock import patch
import pandas as pd

import src
from src.csv_pandas import read_from_csv, read_from_excel


@patch(src.csv_pandas.pd.read_csv)
def test_read_from_csv(mock_pd_read_csv, datas):
    """Функция, тестирующая функцию чтения данных из CSV-файла"""
    mock_pd_read_csv.return_value = datas.to_dict(orient="records")
    assert read_from_csv("id,state\\n50,EXECUTED\\n10,CANCELED") == [
        {"ID": "50", "state": "EXECUTED"},
        {"ID": "10", "state": "CANCELED"},
    ]


def test_2_read_from_csv():
    assert read_from_csv("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\transaction") == []


@patch(src.csv_pandas.pd.read_excel)
def test_read_from_excel(mock_pd_read_excel):
    """Функция, тестирующая функцию чтения данных из excel-файла"""
    ex_datas = "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\test_transactions_excel.xlsx"
    mock_pd_read_excel.return_value = pd.read_excel(ex_datas)
    assert read_from_excel(ex_datas) == (4, 2)
