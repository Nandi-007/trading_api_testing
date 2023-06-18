import asyncio

import trading_ms_steps


def test_receive_ws_messages():
    asyncio.get_event_loop().run_until_complete(trading_ms_steps.send_ws_message())
    #asyncio.get_event_loop().run_until_complete(core.receive_ws_messages())
