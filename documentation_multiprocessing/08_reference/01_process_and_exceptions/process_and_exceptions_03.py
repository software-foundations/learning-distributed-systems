import multiprocessing as mp


def f() -> None:

	print(f'\nprocess: {mp.current_process().name}')

def main() -> None:

	[mp.Process(name=f'{i}', target=f).start() for i in range(100)]

if __name__ == '__main__':

	main()
