from multiprocessing import Pool


NUMBER_PARALELL_PROCESSESS: int = 2

N_ENTRIES: int = 200

def target_function(number: float) -> None:

	return number

if __name__ == '__main__':
	
	with Pool(processes=NUMBER_PARALELL_PROCESSESS) as p:

		print(p.map(func=target_function, iterable=range(N_ENTRIES)))