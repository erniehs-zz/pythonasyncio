from multiprocessing import Pool
import time

COUNT = 50000000
PROCESSES = 4


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=PROCESSES)
    start = time.time()
    for _ in range(PROCESSES):
        pool.apply_async(countdown, [COUNT // PROCESSES])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
