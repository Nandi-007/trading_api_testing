import pytest

import trading_ms_steps


def test_delete_order_orderid():
    response = trading_ms_steps.post_new_order(trading_ms_steps.dummy_order_data)
    assert response.status_code == 201
    order = response.json()

    assert order.get("id") is not None
    assert order.get("stoks") == trading_ms_steps.dummy_order_data["stoks"]
    assert order.get("quantity") == trading_ms_steps.dummy_order_data["quantity"]
    assert order.get("status") == "pending"

    response = trading_ms_steps.delete_order_by_id(order.get("id"))
    assert response.status_code == 204
    response = trading_ms_steps.get_order_by_id(order.get("id"))
    assert response.status_code == 200
    response_order = response.json()
    assert response_order.get("id") == order.get("id")
    assert response_order.get("stoks") == order.get("stoks")
    assert response_order.get("quantity") == order.get("quantity")
    assert response_order.get("status") == "canceled"


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
def test_delete_order_orderid_404(order_data):
    response = trading_ms_steps.delete_order_by_id(order_data["id"])
    assert response.status_code == 404
    order = response.json()
    assert order.get("description") == "Order with id {} not found".format(order_data["id"])
