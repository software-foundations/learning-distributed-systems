"""
asyncio.create_task(coro, *, name=None)

Wrap the coro coroutine into Task and schedule its execution
Return the Task object.

if name is not None, it is set as the name of the task
using Task.set_name().

The task is executed in the loop returned by
get_running_loop(), RuntimeError is raised if there is no
running loop in current thread

This function has been added in Python 3.7

Changed in version 3.8: Added the name parameter.

This function has been added in Python 3.7. Prior to Python 
3.7, the low-level asyncio.ensure_future() function can be 
used instead:
"""
import asyncio


async def coro():
    ...

# Python 3.7+
task = asyncio.create_task(coro())

# This works in all Python versions but is less readable
task = asyncio.ensure_future(coro())
