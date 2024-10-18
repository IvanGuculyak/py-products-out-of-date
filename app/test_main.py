from app.main import outdated_products
from unittest import mock
import datetime
import pytest


PRODUCT_LIST = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }
]


@pytest.mark.parametrize(
    "today, outdated_products_list",
    [
        (datetime.date(2022, 1, 1), []),
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
def test_outdated_products(
    today: datetime.date,
    outdated_products_list: list,
) -> None:
    with mock.patch("datetime.date") as mock_today:
        mock_today.today.return_value = today
        assert outdated_products(PRODUCT_LIST) == outdated_products_list
