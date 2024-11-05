from unittest.mock import patch

import pytest

from src.external_api import get_currency


@patch("requests.get")
def test_get_currency(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "info": {"rate": 90, "timestamp": 1519328414},
        "query": {"amount": 25, "from": "USD", "to": "RUB"},
        "result": 900,
        "success": True,
    }

    result = get_currency("RUB", "USD", 10)
    assert result == 900
    mock_get.assert_called()


with pytest.raises(Exception):
    get_currency("RRR")
