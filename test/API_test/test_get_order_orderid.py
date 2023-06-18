import pytest

import trading_ms_steps


def test_get_order_orderid_200():
    response = trading_ms_steps.post_new_order(trading_ms_steps.dummy_order_data)
    order = response.json()
    response = trading_ms_steps.get_order_by_id(order.get("id"))
    assert response.status_code == 200
    order = response.json()
    assert order.get("id") == order.get("id")
    assert order.get("stoks") == trading_ms_steps.dummy_order_data["stoks"]
    assert order.get("quantity") == trading_ms_steps.dummy_order_data["quantity"]
    assert order.get("status") == "pending"


@pytest.mark.parametrize("order_data", [
    {"id": "0"},
    {"id": "invalid"},
    {"id": "-1"},
    {"id": "1.6"},
    {"id": None},
    {"id": "order123"},
    {"id": "@$%"},
    {"id": " "},
    {"id": "1" * 101},
])
def test_get_order_orderid_404(order_data):
    response = trading_ms_steps.get_order_by_id(order_data["id"])
    assert response.status_code == 404
    order = response.json()
    assert order.get("description") == "Order with id {} not found".format(order_data["id"])
