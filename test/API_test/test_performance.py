import concurrent.futures
import time
import statistics
import asyncio

import trading_ms_steps
import websockets

NUMBER_OF_REQUESTS = 100


async def place_order_and_receive_message():
    async with websockets.connect(trading_ms_steps.WS_URL) as websocket:
        await websocket.send("Place order")
        start_time = time.time()
        response = trading_ms_steps.post_new_order(trading_ms_steps.dummy_order_data)
        ws_response = await websocket.recv()
        assert ws_response == "Message text was: Place order"
        end_time = time.time()

        return response, start_time, end_time


def test_performance_test():
    order_delays = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(asyncio.run, place_order_and_receive_message()) for _ in range(NUMBER_OF_REQUESTS)]

        # Wait for all futures to complete
        concurrent.futures.wait(futures)

        # Get the results of each completed future
        results = [future.result() for future in futures]

        for result, start_time, end_time in results:
            assert result.status_code == 201
            order = result.json()
            assert order.get("id") is not None
            assert order.get("stoks") == trading_ms_steps.dummy_order_data["stoks"]
            assert order.get("quantity") == trading_ms_steps.dummy_order_data["quantity"]
            assert order.get("status") == "pending"

            order_delay = end_time - start_time
            order_delays.append(order_delay)

    # Calculate average order execution delay
    average_delay = sum(order_delays) / len(order_delays)

    # Calculate standard deviation of order execution delay
    std_deviation = statistics.stdev(order_delays)

    # Print metrics to the console
    print(f"Number of Requests: {NUMBER_OF_REQUESTS}")
    print(f"Average Order Execution Delay: {average_delay:.3f} seconds")
    print(f"Standard Deviation: {std_deviation:.3f} seconds")
