import asyncio


async def task(sleep: int) -> None:

	await asyncio.sleep(sleep)

	print(f'sleep {sleep} ok')


async def main():
	
	task_1 = asyncio.create_task(task(sleep=5))

	task_2 = asyncio.create_task(task(sleep=1))

	await task_1

	await task_2

	print('End')


asyncio.run(main())