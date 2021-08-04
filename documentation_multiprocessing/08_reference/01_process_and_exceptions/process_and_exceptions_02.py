import multiprocessing as mp


def target_function() -> None:

	print(f'\nprocess: {mp.current_process().name}')

def main() -> None:

	for i in range(100):
		
		process = mp.Process(
			name=f'process {i}', 
			target=target_function)

		process.start()

if __name__ == '__main__':
	
	main()
