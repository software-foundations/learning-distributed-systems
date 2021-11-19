import asyncio


# There are three main types of awaitable objects: 
# coroutines, Tasks, and Futures.

##############
# Coroutines #

# Python coroutines are awaitables and therefore 
# can be awaited from other coroutines:

# In other words: nested coroutines!!!
##############

async def coroutine_2() -> None:

    print('coroutine 2 starts')

    await asyncio.sleep(2)

async def coroutine_1() -> None:

    print('coroutine 1 starts')

    await coroutine_2()

    print('coroutine 2 ends')

async def main() -> None:

    await coroutine_1()

    print('coroutine 1 ends')

asyncio.run(main())
