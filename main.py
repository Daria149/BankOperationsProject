from src.masks import get_mask_account, get_mask_card_number
from src.processing import sort_by_date

from src.widget import get_date
from src.utils import transactions_sum, get_operations_transactions

print(get_mask_card_number(7000792289606361))

print(get_mask_account("73654108430135874305"))

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

print(get_date("2024-03-11T02:26:18.671407"))


if __name__ == "__main__":
    print(transactions_sum(
            get_operations_transactions(
                "C:/Users/Darya/Desktop/ProjectsHometasks/BankOperationsProject/data/operations.json"
            )
        )
    )