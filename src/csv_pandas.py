import logging
from typing import Any

import pandas as pd

reading_logger = logging.getLogger("csv_pandas")
f_handler = logging.FileHandler(
    "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\BankOperationsProject\\logs\\csv_pandas.log",
    mode="w",
    encoding="utf-8",
)
file_formatter = logging.Formatter("%(filename)s % (levelname)s: %(message)s")
f_handler.setFormatter(file_formatter)
reading_logger.addHandler(f_handler)
reading_logger.setLevel(logging.INFO)


def read_from_csv(file_path: str) -> Any:
    """Функция, читающая данные из CSV-файла"""
    try:
        d_reader = pd.read_csv(file_path, delimiter=";")
    except FileNotFoundError:
        logging.error("Файл не найден")
        return []
    dict_reader = d_reader.to_dict(orient="records")
    return dict_reader


def read_from_excel(file_path: str) -> Any:
    """Функция, читающая данные из CSV-файла"""
    try:
        datas = pd.read_excel(file_path)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return []
    logging.info("Файл читается")
    dict_datas = datas.to_dict(orient="records")
    return dict_datas