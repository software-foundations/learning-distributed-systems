"""
Future

Is a special low level awaitable object that represents an
eventual result of an asynchronous operation.

When a Future object is awaitable it means that the
coroutine will wait until the Future is resolved in
some other place.

Future objects in asyncio are needed to allow callback-based
code to be used with async/await.

Normally there is no need to create Future objects at the
application level code.

Future objects, sometimes exposed by libraries and some
asyncio APIs, can be awaited.
"""
import asyncio

async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
