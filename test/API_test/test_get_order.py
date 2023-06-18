import trading_ms_steps


def test_get_orders():
    order_id = 1
    response = trading_ms_steps.get_orders()
    assert response.status_code == 200
    orders = response.json()
    number_od_elements = len(orders)
    for order in orders:
        assert order.get("id") == f"{order_id}"
        assert order.get("stoks") in ["EUR", "USD", "GBP"]
        assert isinstance(order.get("quantity"), float) or order.get("quantity") <= 0
        assert order.get("status") in ["canceled", "pending", "executed"]
        order_id += 1

    response = trading_ms_steps.post_new_order(trading_ms_steps.dummy_order_data)
    assert response.status_code == 201
    order = response.json()

    assert order.get("id") is not None
    assert order.get("stoks") == trading_ms_steps.dummy_order_data["stoks"]
    assert order.get("quantity") == trading_ms_steps.dummy_order_data["quantity"]
    assert order.get("status") == "pending"

    response = trading_ms_steps.get_orders()
    assert response.status_code == 200
    orders = response.json()
    number_of_elements_after = len(orders)
    assert number_of_elements_after == number_od_elements + 1
