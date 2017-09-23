import math
import time

# PEP 484

def A(n):
    baselsum = 0;
    for i in range(1,n):
        baselsum += 1.0 / (i * i)
    return math.sqrt(6.0 * baselsum)


def B(n : int) -> float:
    n = float(n)
    baselsum  = 0
    i = 1
    while i < n:
        baselsum += 1.0 / (i * i)
        i += 1
    return math.sqrt(6.0 * baselsum)


if __name__ == '__main__':
    n = 10000000
    start_time = time.time()
    B(n)
    print("A: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    A(n)
    print("B: %s seconds ---" % (time.time() - start_time))

    # A: 2.3665130138397217 seconds ---
    # B: 1.4993691444396973 seconds ---
