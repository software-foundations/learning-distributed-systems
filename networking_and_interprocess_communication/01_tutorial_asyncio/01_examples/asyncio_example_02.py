import asyncio


async def get_input() -> None:

	enter = input('say something: ')	

	print(f'you say {enter}')

async def main():

	print('Hello')	

	await get_input()

	print('End!')

asyncio.run(main())
