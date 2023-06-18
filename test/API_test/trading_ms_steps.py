import requests
import websockets

BASE_URL = "http://172.17.0.2:8080"
WS_URL = "ws://172.17.0.2:8080/ws"

dummy_order_data = {"stoks": "EUR", "quantity": 1000.0}


async def receive_ws_messages():
    async with websockets.connect(WS_URL) as websocket:
        while True:
            response = await websocket.recv()
            assert response != ""


async def send_ws_message():
    async with websockets.connect(WS_URL) as websocket:
        message = "Hello, WebSocket Server!"
        await websocket.send(message)

        response = await websocket.recv()
        assert response == "Message text was: Hello, WebSocket Server!"


def get_orders():
    return requests.get(f"{BASE_URL}/orders")


def get_order_by_id(order_id):
    return requests.get(f"{BASE_URL}/orders/{order_id}")


def post_new_order(order_data):
    return requests.post(f"{BASE_URL}/orders", json=order_data)


def delete_order_by_id(order_id):
    return requests.delete(f"{BASE_URL}/orders/{order_id}")
