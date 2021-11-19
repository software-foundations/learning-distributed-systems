import asyncio
from time import sleep


# Tasks

# Tasks are used to schedule coroutines concurrently.

# When a coroutine is wrapped into a Task with functions like 
# asyncio.create_task() the coroutine is automatically scheduled to run soon

async def coroutine(iteration: int) -> None:

    print(f'coroutine {iteration} starts')  

async def main() -> None:

    print('main starts')

    for i in range(20):

        # "task" can now be used to cancel "voroutine()", or
        # can simply be awaited to wait until it is complete:

        task = asyncio.create_task(coro=coroutine(iteration=i))

        await task

        print(f'coroutine {i} ends')

asyncio.run(main())
