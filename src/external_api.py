import os
from typing import Union

import requests
from dotenv import load_dotenv


def get_currency(to_c: str, from_c: str, parameter: Union[int, float]) -> float:
    """функция конвертации транзакции с использованием API """
    load_dotenv()
    apikey = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_c}&from={from_c}&amount={parameter}"
    headers = {"apikey": apikey}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"{response.status_code}")
    else:
        data = response.json()
        amount = round(data["result"], 2)
        return amount
