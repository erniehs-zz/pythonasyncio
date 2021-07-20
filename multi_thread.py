import time
from threading import Thread

THREADS = 4
COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


threads = [Thread(target=countdown, args=(COUNT // THREADS,))
           for _ in range(THREADS)]

start = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
end = time.time()

print('Time taken in seconds -', end - start)
