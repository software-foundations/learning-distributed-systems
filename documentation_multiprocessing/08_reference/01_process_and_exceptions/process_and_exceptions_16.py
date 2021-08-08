import multiprocessing as mp
import time
import signal


p = mp.Process(target=time.sleep, args=(1000,))

print(p, p.is_alive())

p.start()

print(p, p.is_alive())

p.terminate()

time.sleep(0.1)

print(p, p.is_alive())

print(p.exitcode == -signal.SIGTERM, p.exitcode, -signal.SIGTERM)

print(signal.SIGTERM)

print(-signal.SIGTERM)
