import pytest

import trading_ms_steps


@pytest.mark.parametrize("order_data", [
    {"stoks": "EUR", "quantity": 1.5},
    {"stoks": "USD", "quantity": 500},
    {"stoks": "GBP", "quantity": 2000},
])
def test_post_order_201(order_data):
    response = trading_ms_steps.post_new_order(order_data)
    assert response.status_code == 201
    order = response.json()

    assert order.get("id") is not None
    assert order.get("stoks") == order_data["stoks"]
    assert order.get("quantity") == order_data["quantity"]
    assert order.get("status") == "pending"


@pytest.mark.parametrize("order_data", [
    {"stoks": "dollar", "quantity": 1000},
    {"stoks": "USD", "quantity": 0},
    {"stoks": "GBP", "quantity": -1},
    {"stoks": "GBP", "quantity": -1.1},
    {"stoks": "GBP", "quantity": "asdf"},
    {"stoks": "GBP", "quantity": "%%%"},
    {"stoks": None, "quantity": 1000},
    {"stoks": "", "quantity": 1000},
    {"stoks": " ", "quantity": 1000},
    {"stoks": "GBP", "quantity": None},
    {"stoks": "GBP", "quantity": ""},
    {"stoks": "GBP", "quantity": " "},
])
def test_post_order_400(order_data):
    response = trading_ms_steps.post_new_order(order_data)
    assert response.status_code == 400
    order = response.json()

    assert order.get("detail") == "Invalid input"
