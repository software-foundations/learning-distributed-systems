"""
If result is provided, it is returned to the caller when 
the coroutine completes.

sleep() always suspends the current task, allowing other 
tasks to run.

Setting the delay to 0 provides an optimized path to allow
other tasks to run. This can be used by long-running 
functions to avoid blocking the event loop for tor the
duration of the function call.

Deprecated since version 3.8, removed in version 3.10: The 
loop parameter. This function has been implicitly getting
the current running loop since 3.7.

Example of coroutine displaying the current date every
second for 5 seconds:
"""
import asyncio
import datetime


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while true:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())