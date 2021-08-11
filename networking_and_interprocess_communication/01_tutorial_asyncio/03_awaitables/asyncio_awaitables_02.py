import asyncio
from tqdm import trange
from time import sleep


async def coroutine() -> str:	

	print('coroutine starts')

	for _ in trange(10):

		sleep(1)

	return 'ok'	

async def main() -> None:

	print('main starts')

	value = await coroutine()

	print(f'awaited value: {value}')

asyncio.run(main())
