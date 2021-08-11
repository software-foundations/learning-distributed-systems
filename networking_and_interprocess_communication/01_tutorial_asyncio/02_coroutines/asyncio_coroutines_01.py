import asyncio

# Mechanism 01

async def some_processing() -> None:

	print('start processing')

	await asyncio.sleep(3)	

async def main():

	await some_processing()

	print('Processed')

asyncio.run(main())
