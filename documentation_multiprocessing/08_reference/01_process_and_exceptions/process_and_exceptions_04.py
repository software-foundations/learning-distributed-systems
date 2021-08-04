import multiprocessing as mp
from random import randint
from typing import Iterator


N_ITERATIONS: int = 100

def target(a: float, b: float) -> None:

	print(f'\n{mp.current_process().name} -> {a * b}')

def calc_list(n_iterations: int) -> None:

	return [randint(0, 100) for _ in range(n_iterations)]

def calc_zip_list(n_iterations: int) -> Iterator:

	return zip(range(n_iterations), calc_list(n_iterations), calc_list(n_iterations))

def main() -> None:

	for i, a, b in calc_zip_list(n_iterations=N_ITERATIONS):

		mp.Process(
			name=f'process {i} : ({a} x {b})', 
			target=target,
			args=(a, b,)).start()

if __name__ == '__main__':

	main()
